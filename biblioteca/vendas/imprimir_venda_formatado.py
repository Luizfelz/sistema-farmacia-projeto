def imprimir_venda_formatado(registro_venda: str, venda_dict):
    if registro_venda in venda_dict.keys():
      venda = venda_dict[registro_venda]
      representacao = f'\nData e Hora: {venda.data_venda} às {venda.hora_venda}\n'
      representacao += f'Cliente: {venda.cpf_cliente.cpf[0:4]}' + '*******\n'
      produtos = list(venda.produtos_vendidos.keys())
      lista_produtos = []
      for produto in produtos:
         lista_produtos.append(produto.nome)
      quantidades = list(venda.produtos_vendidos.values())
      quantidade_produtos = dict(zip(lista_produtos, quantidades))
      representacao += f'Quantidade de produtos: {quantidade_produtos}\n'
      representacao += f'Valor total da venda: R$ {venda.valor_total:.2f}'
      print(representacao)
    else:
        print('Não existem vendas feitas para o cliente e data informados!')