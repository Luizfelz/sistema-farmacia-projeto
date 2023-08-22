from datetime import datetime, timedelta
from biblioteca.clientes.cadastro_cliente import CadastroCliente
from biblioteca.medicamentos.cadastro_medicamento import CadastroMedicamento
from biblioteca.vendas.vendas import Vendas
from biblioteca.vendas.imprimir_venda_formatado import imprimir_venda_formatado
from biblioteca.medicamentos.imprimir_medicamento_formatado import imprimir_medicamento_formatado

VALOR_VENDA_PARA_DESCONTO = 150
DESCONTO_PERCENTUAL_VENDA_ACIMA_150_REAIS = 0.1
IDADE_PARA_DESCONTO_NA_VENDA = 65
DESCONTO_PERCENTUAL_VENDA_CLIENTE_ACIMA_65_ANOS = 0.2
TAMANHO_REGISTRO_VENDA = 15

class CadastroVenda:

    qntd_atendimentos_realizados_no_dia = 0
    qntd_medicamento_quimio_vendido_no_dia = 0
    valor_total_quimio_vendido_no_dia = 0
    qntd_medicamento_fito_vendido_no_dia = 0
    valor_total_fito_vendido_no_dia = 0
    cadastro_todas_vendas_dict = {}
    medicamento_mais_vendido_no_dia = {}

    def cadastrar_nova_venda() -> None:
        carrinho_de_compra = {}
        valor_total_venda = 0
        quantidade_produtos_carrinho = 0
        data_agora = datetime.now()
        data_venda = str(data_agora.day).zfill(2) + '/' + str(data_agora.month).zfill(2) + '/' + str(data_agora.year)
        hora_venda = str(data_agora.hour) + ':' + str(data_agora.minute).zfill(2)
        buscar_cpf_cliente = input('Digite o CPF do cliente que fará a compra (sem pontuação | ex: 12345678900): ')
        
        if buscar_cpf_cliente in CadastroCliente.cadastros_clientes_dict.keys():
            cliente = CadastroCliente.cadastros_clientes_dict[buscar_cpf_cliente]
            CadastroVenda.qntd_atendimentos_realizados_no_dia += 1
            fechar_carrinho_compra = True
            while fechar_carrinho_compra:
                nome_produto = input('Digite o nome do medicamento que deseja adicionar ao carrinho [ou digite 0 (zero) para fechar o carrinho]: ')
                
                if nome_produto == '0' or nome_produto == 'zero':
                    fechar_carrinho_compra = False
                    print(f'Carrinho de compra fechado!\n')
                elif nome_produto in CadastroMedicamento.cadastro_todos_medicamentos_dict.keys():
                    medicamento = CadastroMedicamento.cadastro_todos_medicamentos_dict[nome_produto]
                    tipo_medicamento = medicamento.tipo
                    imprimir_medicamento_formatado(medicamento)
                    adicionar_ao_carrinho = input('O medicamento acima é o que você deseja adicionar ao carrinho [S | N]? ').lower()
                    
                    if adicionar_ao_carrinho in ('sim', 's'):
                        if medicamento.receita == True:
                            alerta_necessidade_receita = input(f'ALERTA! O medicamento [{medicamento.nome.upper()}] requer apresentação de receita.\nO cliente possui a receita para a compra do medicamento [S | N]? ').lower()
                            if alerta_necessidade_receita in ('sim', 's'):
                                quantidade = int(input('Qual a quantidade desse produto que você deseja adicionar ao carrinho? '))
                                if CadastroMedicamento.cadastro_todos_medicamentos_dict.get(nome_produto) in carrinho_de_compra.keys():
                                    carrinho_de_compra[CadastroMedicamento.cadastro_todos_medicamentos_dict[nome_produto]] += quantidade
                                    valor_total_venda += (CadastroMedicamento.cadastro_todos_medicamentos_dict[nome_produto].valor_medicamento) * quantidade
                                    quantidade_produtos_carrinho += quantidade
                                    print('Produto(s) adicionado(s) ao carrinho com sucesso!\n')
                                else:
                                    carrinho_de_compra[CadastroMedicamento.cadastro_todos_medicamentos_dict[nome_produto]] = quantidade
                                    valor_total_venda += (CadastroMedicamento.cadastro_todos_medicamentos_dict[nome_produto].valor_medicamento) * quantidade
                                    quantidade_produtos_carrinho += quantidade
                                    print('Produto(s) adicionado(s) ao carrinho com sucesso!\n')
                            else:
                                print('É necessária a apresentação de receita para compra deste medicamento!\nProduto não adicionado do carrinho de compra!\n')
                        else:
                            quantidade = int(input('Qual a quantidade desse produto que você deseja adicionar ao carrinho? '))
                            if CadastroMedicamento.cadastro_todos_medicamentos_dict.get(nome_produto) in carrinho_de_compra.keys():
                                carrinho_de_compra[CadastroMedicamento.cadastro_todos_medicamentos_dict[nome_produto]] += quantidade
                                valor_total_venda += (CadastroMedicamento.cadastro_todos_medicamentos_dict[nome_produto].valor_medicamento) * quantidade
                                quantidade_produtos_carrinho += quantidade
                                print('Produto(s) adicionado(s) ao carrinho com sucesso!\n')
                            else:
                                carrinho_de_compra[CadastroMedicamento.cadastro_todos_medicamentos_dict[nome_produto]] = quantidade
                                valor_total_venda += (CadastroMedicamento.cadastro_todos_medicamentos_dict[nome_produto].valor_medicamento) * quantidade
                                quantidade_produtos_carrinho += quantidade
                                print('Produto(s) adicionado(s) ao carrinho com sucesso!\n')
                else:
                    print('Este medicamento não está cadastrado. Verifique o nome digitado!\n')
            idade_cliente = (datetime.now() - cliente.data_nascimento) // timedelta(days=365.2425)
            
            if idade_cliente > IDADE_PARA_DESCONTO_NA_VENDA:
                print('\nCliente acima de 65 anos: será aplicado desconto de 20% na venda!')
                print(f'O valor total da venda é: R$ {valor_total_venda:.2f}.')
                total_desconto = (valor_total_venda * DESCONTO_PERCENTUAL_VENDA_CLIENTE_ACIMA_65_ANOS)
                print(f'Desconto de 20% aplicado: - R$ {total_desconto:.2f}')
                valor_total_venda -= total_desconto
                print(f'O valor final da venda é: R$ {valor_total_venda:.2f}.')
            else:
                if valor_total_venda > VALOR_VENDA_PARA_DESCONTO:
                    print('\nCompra acima de R$ 150,00: será aplicado desconto de 10% na venda!')
                    print(f'O valor total da venda é: R$ {valor_total_venda:.2f}.')
                    total_desconto = (valor_total_venda * DESCONTO_PERCENTUAL_VENDA_ACIMA_150_REAIS)
                    print(f'Desconto de 10% aplicado: - R$ {total_desconto:.2f}')
                    valor_total_venda -= total_desconto
                    print(f'O valor total da venda é: R$ {valor_total_venda:.2f}.')
                else:
                    print(f'\nO valor total da venda é: R$ {valor_total_venda:.2f}.')
            finalizar_venda = input('\nDigite [1] para finalizar a venda ou [0] para cancelar a venda: ')
            
            if finalizar_venda == '1':
                registro_venda = str(cliente.cpf[0:4]) + '-' + str(data_venda)
                print(f'\nVenda [{registro_venda}] finalizada com sucesso!')
                CadastroVenda.cadastro_todas_vendas_dict[registro_venda] = Vendas(data_venda, hora_venda, carrinho_de_compra, cliente, valor_total_venda)
                for item in carrinho_de_compra.keys():
                    if item.tipo == 'fitoterápico':
                        CadastroVenda.qntd_medicamento_fito_vendido_no_dia += carrinho_de_compra[item]
                        CadastroVenda.valor_total_fito_vendido_no_dia += (item.valor_medicamento * carrinho_de_compra[item])
                    elif item.tipo == 'quimioterápico':
                        CadastroVenda.qntd_medicamento_quimio_vendido_no_dia += carrinho_de_compra[item]
                        CadastroVenda.valor_total_quimio_vendido_no_dia += (item.valor_medicamento * carrinho_de_compra[item])
                for item in carrinho_de_compra.keys():
                    if item.nome not in CadastroVenda.medicamento_mais_vendido_no_dia.keys():
                        CadastroVenda.medicamento_mais_vendido_no_dia[item.nome] = carrinho_de_compra[item]
                    else:
                        CadastroVenda.medicamento_mais_vendido_no_dia[item.nome] += carrinho_de_compra[item]
            else:
                print('Venda cancelada!')
        else:
            print(f'Cliente com CPF: {buscar_cpf_cliente} não cadastrado! Por favor, cadastre o cliente e tente novamente.')
    
    def visualizar_venda() -> None:
        pesquisa_venda_cpf = input('Digite os 4 primeiros dígitos do CPF do cliente que fez a compra: ')
        pesquisa_venda_data = input('Digite a data da compra [ex: 01/01/2001]: ')
        registro_venda = pesquisa_venda_cpf + '-' + pesquisa_venda_data
        if len(registro_venda) != TAMANHO_REGISTRO_VENDA:
            print('Erro nas informações informadas. Por favor, verifique os dados e tente novamente! \n')
            return 
        venda_dict = CadastroVenda.cadastro_todas_vendas_dict
        imprimir_venda_formatado(registro_venda, venda_dict)