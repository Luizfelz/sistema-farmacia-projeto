from biblioteca.laboratorios.laboratorio import Laboratorio
from biblioteca.medicamentos.medicamento import MedicamentoFitoterapico
from biblioteca.medicamentos.medicamento import MedicamentoQuimioterapico
from biblioteca.laboratorios.cadastro_laboratorio import CadastroLaboratorio
from biblioteca.medicamentos.imprimir_medicamento_formatado import imprimir_medicamento_formatado

class CadastroMedicamento:

    quantidade_medicamento_cadastrado_total = 0
    cadastro_todos_medicamentos_dict = {}

    def cadastrar_medicamento() -> None:
        nome = input('Digite o nome do medicamento: ').lower()
        if nome not in CadastroMedicamento.cadastro_todos_medicamentos_dict.keys():
            principal_composto = input('Digite o nome do principal composto do medicamento: ').lower()
            laboratorio = input('Digite o laboratório do medicamento: ').lower()
            descricao = input('Digite a descrição do medicamento: ').lower()
            tipo_medicamento_valido = False
            while not tipo_medicamento_valido:
                tipo = input('Este medicamento é Quimioterápico (digite Q) ou Fitoterápico (digite F)? ').lower()
                if tipo == 'f' or tipo == 'q':
                    tipo_medicamento_valido = True
                else:
                    print('\n Tipo inválido.\n')
            receita = input('O medicamento precisa de receita [S | N]? ').lower()
            valor_medicamento = float(input('Qual o valor de venda do medicamento? '))
            if receita.lower() in ['sim','s']:
                receita = True
            else:
                receita = False
            
            if laboratorio not in CadastroLaboratorio.cadastro_todos_laboratorios_dict.keys():
                print(f'\nO laboratório "{laboratorio.upper()}" não consta no banco de dados de laboratórios. Por favor, faça o cadastro do laboratório: \n')
                print(f'Digite o nome do laboratório para cadastro: {laboratorio}')
                nome_laboratorio = laboratorio
                endereco_laboratorio = input('Digite o endereço do laboratório: ').lower()
                telefone_contato = input('Digite o telefone de contato, somente números [ex: 0011112222]: ')
                cidade_laboratorio = input('Digite a cidade: ').lower()
                estado_laboratorio = input('Digite o estado: ').lower()
                novo_laboratorio = Laboratorio(nome_laboratorio, endereco_laboratorio, telefone_contato, cidade_laboratorio, estado_laboratorio)
                CadastroLaboratorio.cadastro_todos_laboratorios_dict[laboratorio] = novo_laboratorio
            else:
                novo_laboratorio = CadastroLaboratorio.cadastro_todos_laboratorios_dict[laboratorio]
            
            if tipo == 'f':
                novo_medicamento = MedicamentoFitoterapico(nome, principal_composto, novo_laboratorio, descricao, receita, valor_medicamento)
                MedicamentoFitoterapico.cadastro_medicamento_fitoterapico_dict[nome] = novo_medicamento
            elif tipo == 'q':
                novo_medicamento = MedicamentoQuimioterapico(nome, principal_composto, novo_laboratorio, descricao, receita, valor_medicamento)
                MedicamentoQuimioterapico.cadastro_medicamento_quimioterapico_dict[nome] = novo_medicamento
            CadastroMedicamento.cadastro_todos_medicamentos_dict[nome] = novo_medicamento
            print('\nCadastro realizado com sucesso!\n')
            CadastroMedicamento.quantidade_medicamento_cadastrado_total += 1
        else:
            print('Este medicamento já está cadastrado!\n')

    def visualizar_medicamento() -> None:
        pesquisa = input('Digite o nome, fabricante, ou alguma outra informação do(s) medicamento(s) que deseja buscar: ').lower()
        nenhum_medicamento_encontrado = True
        for nome in CadastroMedicamento.cadastro_todos_medicamentos_dict.keys():
            medicamento = CadastroMedicamento.cadastro_todos_medicamentos_dict[nome]
            if pesquisa in CadastroMedicamento.cadastro_todos_medicamentos_dict.keys() and pesquisa == nome:
                imprimir_medicamento_formatado(medicamento, pesquisa)
                nenhum_medicamento_encontrado = False
            elif pesquisa in CadastroMedicamento.cadastro_todos_medicamentos_dict[nome].principal_composto:
                imprimir_medicamento_formatado(medicamento, pesquisa)
                nenhum_medicamento_encontrado = False
            elif pesquisa in CadastroMedicamento.cadastro_todos_medicamentos_dict[nome].laboratorio.nome:
                imprimir_medicamento_formatado(medicamento, pesquisa)
                nenhum_medicamento_encontrado = False
            elif pesquisa in CadastroMedicamento.cadastro_todos_medicamentos_dict[nome].descricao:
                imprimir_medicamento_formatado(medicamento, pesquisa)
                nenhum_medicamento_encontrado = False
            elif pesquisa in CadastroMedicamento.cadastro_todos_medicamentos_dict[nome].tipo:
                imprimir_medicamento_formatado(medicamento, pesquisa)
                nenhum_medicamento_encontrado = False
            elif 'receita' in pesquisa:
                precisa_de_receita = True
                nenhum_medicamento_encontrado = False
                for palavra in pesquisa.split():
                    if palavra in ['não', 'sem']:
                        precisa_de_receita = False
                if CadastroMedicamento.cadastro_todos_medicamentos_dict[nome].receita == precisa_de_receita:
                    imprimir_medicamento_formatado(medicamento, pesquisa, pesquisa_por_receita=True)
        if nenhum_medicamento_encontrado == True:
            print('Nenhum medicamento encontrado!')