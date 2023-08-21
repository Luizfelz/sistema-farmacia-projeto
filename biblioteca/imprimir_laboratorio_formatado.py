from biblioteca.cores import Cores

def imprimir_laboratorio_formatado(pesquisa: str, laboratorio):
    laboratorio = laboratorio
    result = f'''
    Nome: {laboratorio.nome}
    Endereço: {laboratorio.endereco}
    Telefone: {laboratorio.telefone_contato}
    Cidade: {laboratorio.cidade}
    Estado: {laboratorio.estado}
    '''
    result = result.replace(pesquisa, Cores.BOLD + Cores.BLUE + pesquisa + Cores.END + Cores.END)
    print(result)