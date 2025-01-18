import Funcoes_sistema as f




def menu_cliente(Sistema_principal: f.clas.SISTEMA, cliente:f.clas.CLIENTE):
    
    if cliente == None or Sistema_principal == None:
        print("Nenhum cliente cadastrado")
        f.pausar_terminal()
        return
    
    while(True):
        f.limpar_terminal()
        
        print(f"Bem vindo cliente {cliente.nome}")
        print("Selecione uma opcao:")
        print("1 - Ver produtos")
        print("2 - Ver carrinho")
        print("3 - Finalizar compra")
        print("4 - Ver historico de compras")
        print("5 - Ver historico de transacoes")
        print("0 - Voltar")
        
        opcao = str(input("Digite a opcao desejada: "))
        
        if opcao == "1":
            pass
        elif opcao == "2":
            pass
        elif opcao == "3":
            pass
        elif opcao == "4":
            pass
        elif opcao == "5":
            pass
        elif opcao == "0":
            break
        else:
            print("Opcao invalida")
            f.pausar_terminal()



def menu_repositor(Sistema_principal: f.clas.SISTEMA, repositor:f.clas.REPOSITOR):
    
    if repositor == None or Sistema_principal == None:
        print("Nenhum repositor cadastrado")
        f.pausar_terminal()
        return
    
    while(True):
        f.limpar_terminal()
        
        print(f"Bem vindo repositor {repositor.nome}")
        print("Selecione uma opcao:")
        print("1 - Ir para estoque")
        print("2 - Ir para prateleira")
        print("3 - Ver sacola")
        print("4 - Ver historico de movimentacao")
        print("0 - Voltar")
        
        opcao = str(input("Digite a opcao desejada: "))
        
        if opcao == "1":
            pass
        elif opcao == "2":
            pass
        elif opcao == "0":
            break
        else:
            print("Opcao invalida")
            f.pausar_terminal()



def menu_gerente(Sistema_principal: f.clas.SISTEMA, gerente:f.clas.GERENTE):
    
    if gerente == None or Sistema_principal == None:
        print("Nenhum gerente cadastrado")
        f.pausar_terminal()
        return
    
    while(True):
        f.limpar_terminal()
        
        print(f"Bem vindo gerente {gerente.nome}")
        print("Selecione uma opcao:")
        print("1 - Adicionar gerente")
        print("2 - Adicionar repositor")
        print("3 - Adicionar cliente")
        print("4 - Adicionar produto")
        print("5 - Adicionar estoque")
        print("6 - Adicionar prateleira")
        print("7 - Verificar estoque")
        print("8 - Verificar prateleira")
        print("9 - Verificar clientes")
        print("10 - Verificar repositores")
        print("11 - Verificar gerentes")
        print("12 - Verificar historico de movimentacao geral")
        print("13 - Verificar historico de compras geral")
        print("14 - Verificar historico de vendas geral")
        print("0 - Voltar")
        
        opcao = str(input("Digite a opcao desejada: "))
        
        if opcao == "1":
            pass
        elif opcao == "2":
            pass
        elif opcao == "3":
            pass
        elif opcao == "4":
            pass
        elif opcao == "5":
            pass
        elif opcao == "6":
            pass
        elif opcao == "7":
            pass
        elif opcao == "0":
            break
        else:
            print("Opcao invalida")
            f.pausar_terminal()




def menu_inicial(Sistema_principal: f.clas.SISTEMA):
    
    while(True):
        f.limpar_terminal()
        
        print("Bem vindo ao sistema de supermercado")
        print("Selecione uma conta para acessar:")
        print("1 - Gerente")
        print("2 - Repositor")
        print("3 - Cliente")
        print("0 - Sair")
        
        opcao = str(input("Digite a opcao desejada: "))
        
        if opcao == "1":
            menu_gerente(Sistema_principal, f.verificar_gerente(Sistema_principal))
        elif opcao == "2":
            menu_repositor(Sistema_principal, f.verificar_repositor(Sistema_principal))
        elif opcao == "3":
            menu_cliente(Sistema_principal, f.verificar_cliente(Sistema_principal))
        elif opcao == "0":
            break
        else:
            print("Opcao invalida")
            f.pausar_terminal()
            
