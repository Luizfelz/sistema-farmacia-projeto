from biblioteca.cadastro_cliente import CadastroCliente
from biblioteca.cadastro_laboratorio import CadastroLaboratorio
from biblioteca.cadastro_medicamento import CadastroMedicamento, MedicamentoFitoterapico, MedicamentoQuimioterapico
from biblioteca.cadastro_venda import CadastroVenda
from biblioteca.limpar_prompt import limpar_prompt
from biblioteca.menu_principal import menu_principal, menu_cliente, menu_laboratorio, menu_medicamento, menu_venda, menu_relatorio
from biblioteca.relatorios import relatorio_atendimento_dia, relatorio_clientes_cadastrados, relatorio_medicamentos_fitoterapicos, relatorio_medicamentos_quimioterapicos, relatorio_todos_medicamentos

def rodar_aplicacao():
    opcao_do_menu = -1
    while opcao_do_menu != 0:
        menu_principal()
        opcao_do_menu = int(input('Digite uma opção: '))
        limpar_prompt()
        if opcao_do_menu == 1:
            rodar_codigo = True
            while rodar_codigo:
                menu_cliente()
                opcao_menu_cliente = int(input('Digite uma opção: '))
                limpar_prompt()
                if opcao_menu_cliente == 1:
                    print('=== Novo cadastro ===\n')
                    CadastroCliente.cadastrar_cliente()
                    print('\n=== Fim do cadastro ===\n')
                elif opcao_menu_cliente == 2:
                    cpf_procurado = input('Qual CPF do cliente que deseja visualizar (sem pontuação | ex: 12345678900)? ')
                    if cpf_procurado not in CadastroCliente.cadastros_clientes_dict.keys():
                        print('Este CPF não está cadastrado!\n')
                    else:
                        print('=== Visualização de cadastrado ===\n')
                        CadastroCliente.visualizar_cadastro(cpf_procurado)
                        print('\n=== Fim da visualização ===\n')
                elif opcao_menu_cliente == 3:
                    print('=== Alterar cadastro ===\n')
                    cpf_a_alterar = input('Digite o CPF a ser alterado (sem pontuação | ex: 12345678900): ')
                    CadastroCliente.alterar_cadastro(cpf_a_alterar)
                    print('\n=== Fim da alteração ===\n')
                elif opcao_menu_cliente == 0:
                    rodar_codigo = False
                else:
                    print('Opção digitada inválida!\n')
        elif opcao_do_menu == 2:
            rodar_codigo = True
            while rodar_codigo:
                menu_medicamento()
                opcao_menu_medicamento = int(input('Digite uma opção: '))
                limpar_prompt()
                if opcao_menu_medicamento == 1:
                    print('=== Novo cadastro de medicamento ===\n')
                    CadastroMedicamento.cadastrar_medicamento()
                    print('\n=== Fim do cadastro ===\n')
                elif opcao_menu_medicamento == 2:
                    print('=== Visualização do(s) medicamento(s) cadastrado(s) ===\n')
                    CadastroMedicamento.visualizar_medicamento()
                    print('\n=== Fim da visualização ===\n')
                elif opcao_menu_medicamento == 0:
                    rodar_codigo = False
                else:
                    print('Opção digitada inválida!\n')
        elif opcao_do_menu == 3:
            rodar_codigo = True
            while rodar_codigo:
                menu_laboratorio()
                opcao_menu_laboratorio = int(input('Digite uma opção: '))
                limpar_prompt()
                if opcao_menu_laboratorio == 1:
                    print('=== Novo cadastro de laboratório ===\n')
                    CadastroLaboratorio.cadastrar_novo_laboratorio()
                    print('\n=== Fim do cadastro ===\n')
                elif opcao_menu_laboratorio == 2:
                    print('===Visualização do(s) laboratório(s) cadastrado(s)===\n')
                    CadastroLaboratorio.visualizar_laboratorio()
                    print('\n=== Fim da visualização ===\n')
                elif opcao_menu_laboratorio == 0:
                    rodar_codigo = False
                else:
                    print('Opção digitada inválida!\n')
        elif opcao_do_menu == 4:
            rodar_codigo = True
            while rodar_codigo:
                menu_venda()
                opcao_menu_venda = int(input('O que deseja fazer? '))
                limpar_prompt()
                if opcao_menu_venda == 1:
                    print('=== Novo cadastro de venda ===\n')
                    CadastroVenda.cadastrar_nova_venda()
                    print('\n=== Fim do cadastro ===\n')
                elif opcao_menu_venda == 2:
                    print('=== Visualização de venda(s) realizada(s) ===\n')
                    CadastroVenda.visualizar_venda()
                    print('\n=== Fim da visualização ===\n')
                elif opcao_menu_venda == 0:
                    rodar_codigo = False
                else:
                    print('Opção digitada inválida!\n')
        elif opcao_do_menu == 5:
           rodar_codigo = True
           while rodar_codigo:
              menu_relatorio()
              opcao_menu_relatorio = int(input('O que deseja fazer? '))
              limpar_prompt()
              if opcao_menu_relatorio == 1:
                  clientes_dict = CadastroCliente.cadastros_clientes_dict
                  print('=== Relatório de Clientes ===\n')
                  relatorio_clientes_cadastrados(clientes_dict)
                  print('\n=== Fim do relatório ===\n')
              elif opcao_menu_relatorio == 2:
                  medicamentos_dict = CadastroMedicamento.cadastro_todos_medicamentos_dict
                  print('=== Relatório de Medicamentos ===\n')
                  relatorio_todos_medicamentos(medicamentos_dict)
                  print('\n=== Fim do relatório ===\n')
              elif opcao_menu_relatorio == 3:
                  medicamentos_quimioterapicos_dict = MedicamentoQuimioterapico.cadastro_medicamento_quimioterapico_dict
                  print('=== Relatório de Medicamentos Quimioterápicos ===\n')
                  relatorio_medicamentos_quimioterapicos(medicamentos_quimioterapicos_dict)
                  print('\n=== Fim do relatório ===\n')
              elif opcao_menu_relatorio == 4:
                  medicamentos_fitoterapicos_dict = MedicamentoFitoterapico.cadastro_medicamento_fitoterapico_dict
                  print('=== Relatório de Medicamentos Fitoterápicos ===\n')
                  relatorio_medicamentos_fitoterapicos(medicamentos_fitoterapicos_dict)
                  print('\n=== Fim do relatório ===\n')
              elif opcao_menu_relatorio == 5:
                  solicitar_relatorio_atendimento_do_dia()
              elif opcao_menu_relatorio == 0:
                  rodar_codigo = False
              else:
                  print('Opção digitada inválida!\n')
        elif opcao_do_menu == 0:
            print('=== Finalização do programa... ===\n')
            imprimir_relatório = input('Deseja imprimir o relatório do dia [S | N]? ').lower()
            if imprimir_relatório in ('sim', 's'):
                solicitar_relatorio_atendimento_do_dia()
            else:
                print('\n=== Programa finalizado! ===\n')
        else:
            print('Opção inválida!\n')

def solicitar_relatorio_atendimento_do_dia():
    medicamento_mais_vendido = CadastroVenda.medicamento_mais_vendido_no_dia
    qntd_atendimentos_realizados_no_dia = CadastroVenda.qntd_atendimentos_realizados_no_dia
    qntd_medicamento_quimio_vendido_no_dia = CadastroVenda.qntd_medicamento_quimio_vendido_no_dia
    valor_total_quimio_vendido_no_dia = CadastroVenda.valor_total_quimio_vendido_no_dia
    qntd_medicamento_fito_vendido_no_dia = CadastroVenda.qntd_medicamento_fito_vendido_no_dia
    valor_total_fito_vendido_no_dia = CadastroVenda.valor_total_fito_vendido_no_dia
    print('=== Relatório de atendimento do dia ===\n')
    relatorio_atendimento_dia(medicamento_mais_vendido, qntd_atendimentos_realizados_no_dia, \
                              qntd_medicamento_quimio_vendido_no_dia, valor_total_quimio_vendido_no_dia, \
                                qntd_medicamento_fito_vendido_no_dia, valor_total_fito_vendido_no_dia)
    print('\n=== Fim do relatório ===\n')