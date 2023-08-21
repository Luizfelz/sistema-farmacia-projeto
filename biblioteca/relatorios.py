def relatorio_clientes_cadastrados(clientes_dict):
    clientes_dict = clientes_dict
    lista_objeto_clientes = []
    for cpf in clientes_dict.keys():
        lista_objeto_clientes.append(clientes_dict[cpf])
    clientes_lista_nomes = []
    for objeto in lista_objeto_clientes:
        clientes_lista_nomes.append(objeto.nome)
    clientes_lista_nomes.sort()
    for nome in clientes_lista_nomes:
        for objeto in lista_objeto_clientes:
            if objeto.nome == nome:
                print(objeto)
                print('\n')

def relatorio_todos_medicamentos(medicamentos_dict):
    medicamentos_dict = medicamentos_dict
    lista_nomes_medicamentos = list(medicamentos_dict.keys())
    lista_nomes_medicamentos.sort()
    lista_objeto_medicamentos = []
    for medicamento in medicamentos_dict.keys():
        lista_objeto_medicamentos.append(medicamentos_dict[medicamento])
    for nome in lista_nomes_medicamentos:
        for objeto in lista_objeto_medicamentos:
            if objeto.nome == nome:
                print(objeto)
                print('\n')

def relatorio_medicamentos_quimioterapicos(medicamentos_quimioterapicos_dict):
    medicamentos_quimioterapicos_dict = medicamentos_quimioterapicos_dict
    lista_nomes_medicamentos = list(medicamentos_quimioterapicos_dict.keys())
    lista_nomes_medicamentos.sort()
    lista_objeto_medicamentos = []
    for medicamento in medicamentos_quimioterapicos_dict.keys():
        lista_objeto_medicamentos.append(medicamentos_quimioterapicos_dict[medicamento])
    for nome in lista_nomes_medicamentos:
        for objeto in lista_objeto_medicamentos:
            if objeto.nome == nome:
                print(objeto)
                print('\n')

def relatorio_medicamentos_fitoterapicos(medicamentos_fitooterapicos_dict):
    medicamentos_fitooterapicos_dict = medicamentos_fitooterapicos_dict
    lista_nomes_medicamentos = list(medicamentos_fitooterapicos_dict.keys())
    lista_nomes_medicamentos.sort()
    lista_objeto_medicamentos = []
    for medicamento in medicamentos_fitooterapicos_dict.keys():
        lista_objeto_medicamentos.append(medicamentos_fitooterapicos_dict[medicamento])
    for nome in lista_nomes_medicamentos:
        for objeto in lista_objeto_medicamentos:
            if objeto.nome == nome:
                print(objeto)
                print('\n')

def relatorio_atendimento_dia(medicamento_mais_vendido, qntd_atendimentos_realizados_no_dia, \
                              qntd_medicamento_quimio_vendido_no_dia, valor_total_quimio_vendido_no_dia, \
                              qntd_medicamento_fito_vendido_no_dia, valor_total_fito_vendido_no_dia):
    medicamento_mais_vendido = medicamento_mais_vendido
    qntd_atendimentos_realizados_no_dia = qntd_atendimentos_realizados_no_dia
    qntd_medicamento_quimio_vendido_no_dia = qntd_medicamento_quimio_vendido_no_dia
    qntd_medicamento_fito_vendido_no_dia = qntd_medicamento_fito_vendido_no_dia
    valor_total_quimio_vendido_no_dia = valor_total_quimio_vendido_no_dia
    valor_total_fito_vendido_no_dia = valor_total_fito_vendido_no_dia
    try:
        valor_maximo = max(medicamento_mais_vendido.values())
    except:
        valor_maximo = 0
    chave_valor_max = {}
    for chaves in medicamento_mais_vendido.keys():
        if medicamento_mais_vendido[chaves] == valor_maximo:
          chave_valor_max[chaves] = valor_maximo
    print(f'O(s) medicamento(s) mais vendido(s) no dia foi(foram): {chave_valor_max}\n')
    print(f'Quantidade de atendimentos realizados: {qntd_atendimentos_realizados_no_dia}\n')
    print(f'Quantidade de medicamentos QUIMIOTERÁPICOS vendidos no dia: {qntd_medicamento_quimio_vendido_no_dia}')
    print(f'Valor total de medicamentos QUIMIOTERÁPICOS vendidos no dia: R$ {valor_total_quimio_vendido_no_dia}\n')
    print(f'Quantidade de medicamentos FITOTERÁPICOS vendidos no dia: {qntd_medicamento_fito_vendido_no_dia}')
    print(f'Valor total de medicamentos FITOTERÁPICOS vendidos no dia: R$ {valor_total_fito_vendido_no_dia}')
