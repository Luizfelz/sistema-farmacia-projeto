from biblioteca.utilitarios.cores import Cores

def imprimir_medicamento_formatado(medicamento, pesquisa: str = '', pesquisa_por_receita=False):
    medicamento = medicamento
    if pesquisa_por_receita == True:
        receita = Cores.BOLD + Cores.BLUE + 'sim' + Cores.END + Cores.END if medicamento.receita else Cores.BOLD + Cores.BLUE + 'não' + Cores.END + Cores.END
    else:
        receita = 'sim' if medicamento.receita else 'não'
    result = f'''
    Nome: {medicamento.nome}
    Principal composto: {medicamento.principal_composto}
    Laboratório: {medicamento.laboratorio.nome}
    Descrição: {medicamento.descricao}
    Tipo: {medicamento.tipo}
    Receita: {receita}
    Valor: R$ {medicamento.valor_medicamento}
    '''
    result = result.replace(pesquisa, Cores.BOLD + Cores.BLUE + pesquisa + Cores.END + Cores.END)
    print(result)