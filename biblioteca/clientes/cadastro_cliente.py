from biblioteca.clientes.cliente import Cliente
from datetime import datetime

TAMANHO_VALIDO_DE_CPF = 11
TAMANHO_VALIDO_PARA_ANO_NASCIMENTO = 4

class CadastroCliente:

    quantidade_clientes_cadastrados = 0
    cadastros_clientes_dict = {}

    def cadastrar_cliente() -> None:
        cpf_valido = False
        while not cpf_valido:
            cpf = input('Digite o CPF do cliente (sem pontuação | ex: 12345678900): ')
            try:
                cpf_somente_numeros = int(cpf)
                cpf_somente_numeros = True
            except:
                print('\nO CPF deve conter somente números!\n')
                cpf_somente_numeros = False
            if (len(cpf) == TAMANHO_VALIDO_DE_CPF) and (cpf_somente_numeros == True):
                cpf_valido = True
            else:
                print('\nO CPF deve conter 11 dígitos numéricos!\n')
        if cpf not in CadastroCliente.cadastros_clientes_dict.keys():
            nome = input('Digite o nome do cliente: ')
            data_nascimento_valida = False
            while not data_nascimento_valida:
                data_nascimento = input('Digite a data de nascimento do cliente [ex: 01/12/1900]: ').split('/')
                if len(data_nascimento[2]) == TAMANHO_VALIDO_PARA_ANO_NASCIMENTO:
                    try:
                        data_nascimento = datetime(int(data_nascimento[2]), int(data_nascimento[1]), int(data_nascimento[0]))
                        data_nascimento_valida = True
                    except:
                        print('\nData de nascimento inválida. Verifique o que foi digitado!\n')
                else:
                    print('\nData de nascimento inválida. Verifique o que foi digitado!\n')
            novo_cliente = Cliente(nome, data_nascimento, cpf)
            CadastroCliente.cadastros_clientes_dict[cpf] = novo_cliente
            print('Cliente cadastrado com sucesso!')
        else:
            print('Esse CPF já está cadastrado!')

    def visualizar_cadastro(cpf_procurado: str) -> None:
        print(CadastroCliente.cadastros_clientes_dict[cpf_procurado])

    def alterar_cadastro(cpf):
        if cpf not in CadastroCliente.cadastros_clientes_dict:
           print('Esse CPF não está cadastrado!')
           return
        cliente = CadastroCliente.cadastros_clientes_dict[cpf]
        alteracao = input('O que deseja alterar [nome, datanasc ou cpf]? ')
        while alteracao.lower() not in ('nome', 'datanasc', 'cpf'):
            alteracao = input('Erro. Digite novamente o que quer alterar [nome, datanasc ou cpf]: ')
        if alteracao == 'nome':
            novo_nome = input('Digite o novo nome: ')
            cliente.nome = novo_nome
        elif alteracao == 'datanasc':
            nova_data_nascimento = input('Digite a nova data de nascimento [ex: 01/12/1900]: ')
            cliente.data_nascimento = nova_data_nascimento
        elif alteracao == 'cpf':
            novo_cpf = input('Digite o novo CPF (sem pontuação | ex: 12345678900): ')
            cliente.cpf = novo_cpf
            CadastroCliente.cadastros_clientes_dict.pop(cpf)
        CadastroCliente.cadastros_clientes_dict[cliente.cpf] = cliente