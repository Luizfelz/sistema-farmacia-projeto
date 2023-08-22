from biblioteca.laboratorios.laboratorio import Laboratorio
from biblioteca.laboratorios.imprimir_laboratorio_formatado import imprimir_laboratorio_formatado

TAMANHO_VALIDO_PARA_TELEFONE = (10, 11)

class CadastroLaboratorio:

    cadastro_todos_laboratorios_dict = {}

    def cadastrar_novo_laboratorio() -> None:
        nome_laboratorio = input('Digite o nome do laboratório para cadastro: ').lower()
        if nome_laboratorio not in CadastroLaboratorio.cadastro_todos_laboratorios_dict.keys():
            endereco_laboratorio = input('Digite o endereço do laboratório: ').lower()
            telefone_valido = False
            while not telefone_valido:
                telefone_contato = input('Digite o telefone de contato, somente números [ex: 0011112222]: ')
                try:
                    telefone_somente_numeros = int(telefone_contato)
                    telefone_somente_numeros = True
                except:
                    print('\nDigite somente números para o telefone!\n')
                    telefone_somente_numeros = False
                if (len(telefone_contato) in TAMANHO_VALIDO_PARA_TELEFONE) and (telefone_somente_numeros == True):
                    telefone_valido = True
                else:
                    print('\nO tamanho do telefone é inválido! Verifique o número digitado!\n')
            cidade_laboratorio = input('Digite a cidade: ').lower()
            estado_laboratorio = input('Digite o estado: ').lower()
            novo_laboratorio = Laboratorio(nome_laboratorio, endereco_laboratorio, telefone_contato, cidade_laboratorio, estado_laboratorio)
            CadastroLaboratorio.cadastro_todos_laboratorios_dict[nome_laboratorio] = novo_laboratorio
            print('Laboratório cadastrado com sucesso!')
        else:
            print('Este laboratório já está cadastrado!')

    def visualizar_laboratorio() -> None:
        pesquisa = input('Digite o nome do laboratório ou alguma outra informação do laboratório que deseja consultar: ').lower()
        nenhum_laboratorio_encontrado = True
        for nome in CadastroLaboratorio.cadastro_todos_laboratorios_dict.keys():
            laboratorio = CadastroLaboratorio.cadastro_todos_laboratorios_dict[nome]
            if pesquisa in CadastroLaboratorio.cadastro_todos_laboratorios_dict.keys() and pesquisa == nome:
                imprimir_laboratorio_formatado(pesquisa, laboratorio)
                nenhum_laboratorio_encontrado = False
            elif pesquisa in CadastroLaboratorio.cadastro_todos_laboratorios_dict[nome].endereco:
                imprimir_laboratorio_formatado(pesquisa, laboratorio)
                nenhum_laboratorio_encontrado = False
            elif pesquisa in CadastroLaboratorio.cadastro_todos_laboratorios_dict[nome].telefone_contato:
                imprimir_laboratorio_formatado(pesquisa, laboratorio)
                nenhum_laboratorio_encontrado = False
            elif pesquisa in CadastroLaboratorio.cadastro_todos_laboratorios_dict[nome].cidade:
                imprimir_laboratorio_formatado(pesquisa, laboratorio)
                nenhum_laboratorio_encontrado = False
            elif pesquisa in CadastroLaboratorio.cadastro_todos_laboratorios_dict[nome].estado:
                imprimir_laboratorio_formatado(pesquisa, laboratorio)
                nenhum_laboratorio_encontrado = False
        if nenhum_laboratorio_encontrado == True:
            print('Nenhum laboratório encontrado!')