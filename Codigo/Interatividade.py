import Funcoes_sistema as f


def menu_sacola(Sistema_principal: f.clas.SISTEMA, sacola: f.clas.SACOLA_DE_PRODUTOS):
    pass


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
        
        f.limpar_terminal()
        
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


def menu_prateleira_repositor(Sistema_principal: f.clas.SISTEMA, repositor:f.clas.REPOSITOR, prateleira:f.clas.PRATELEIRA):
    
    while(True):
        f.limpar_terminal()
        
        print(f"Bem vindo a prateleira {prateleira.nome}")
        print("Selecione uma opcao:")
        print("1 - Adicionar na prateleira")
        print("2 - pegar na prateleira")
        print("3 - Ver produtos")
        print("0 - Voltar")
        
        opcao = str(input("Digite a opcao desejada: "))
        
        f.limpar_terminal()
        
        if opcao == "1":
            produto = f.verificar_sacola(repositor.sacola)
            
            if produto != None:
                prateleira.adicionar_produto(produto[0], produto[1][0])
                repositor.sacola.remover_produto(produto[0], produto[1][0])
                repositor.adicionar_historico_movimentacao_pessoal("Adicionou", produto[0], produto[1][0], prateleira)
                Sistema_principal.adicionar_movimentacao_geral(str(repositor), prateleira ,"Adicionou",produto[0], produto[1][0])
        
        elif opcao == "2":
            produto = f.verificar_produto_prateleira(prateleira)
            
            if produto != None:
                repositor.sacola.adicionar_produto(produto[0], produto[1], prateleira) 
                prateleira.pegar_produto(produto[0], produto[1])
                repositor.adicionar_historico_movimentacao_pessoal("Retirou", produto[0], produto[1], prateleira)
                Sistema_principal.adicionar_movimentacao_geral(str(repositor), prateleira ,"Retirou",produto[0], produto[1])
        
        elif opcao == "3":
            prateleira.exibir_produtos()
            f.pausar_terminal()
            
        elif opcao == "0":
            break
        else:
            print("Opcao invalida")
            f.pausar_terminal()
    
    
def menu_estoque(Sistema_principal: f.clas.SISTEMA, repositor:f.clas.REPOSITOR ,estoque:f.clas.ESTOQUE):
    
    while(True):
        f.limpar_terminal()
        
        print(f"Bem vindo ao estoque {estoque.nome}")
        print("Selecione uma opcao:")
        print("1 - Adicionar no estoque")
        print("2 - pegar no estoque produto")
        print("3 - Ver produtos")
        print("4 - Ver historico de movimentacao")
        print("0 - Voltar")
        
        opcao = str(input("Digite a opcao desejada: "))
        
        f.limpar_terminal()
        
        if opcao == "1":
            produto = f.verificar_sacola(repositor.sacola)
            
            if produto != None:
                estoque.adicionar_produto(produto[0], produto[1][0])
                repositor.sacola.remover_produto(produto[0], produto[1][0])
                repositor.adicionar_historico_movimentacao_pessoal("Adicionou", produto[0], produto[1][0], estoque)
                Sistema_principal.adicionar_movimentacao_geral(str(repositor), estoque ,"Adicionou",produto[0], produto[1][0])
        
        elif opcao == "2":
            produto = f.verificar_produto_estoque(estoque)
            
            if produto != None:
                repositor.sacola.adicionar_produto(produto[0], produto[1], estoque)
                estoque.pegar_produto(produto[0], produto[1])
                repositor.adicionar_historico_movimentacao_pessoal("Retirou", produto[0], produto[1], estoque)
                Sistema_principal.adicionar_movimentacao_geral(str(repositor), estoque ,"Retirou",produto[0], produto[1])
            
        elif opcao == "3":
            estoque.exibir_produtos_estoque()
            f.pausar_terminal()
            
        elif opcao == "4":
            print(estoque.historico_movimentacao_estoque)
            f.pausar_terminal()
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
        
        f.limpar_terminal()
        
        if opcao == "1":
            estoque = f.verificar_estoque(Sistema_principal)
            
            if estoque != None:
                menu_estoque(Sistema_principal, repositor,estoque)
        
        elif opcao == "2":
            prateleira = f.verificar_prateleira(Sistema_principal)
            
            if prateleira != None:
                menu_prateleira_repositor(Sistema_principal, repositor, prateleira)
        
        elif opcao == "3":
            menu_sacola(Sistema_principal, repositor.sacola)
            
        elif opcao == "4":
            print(repositor.historico_movimentacao_pessoal)
            f.pausar_terminal()
        
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
        
        f.limpar_terminal()
        
        if opcao == "1":
            f.criar_gerente(Sistema_principal, f.digitar_nome(), f.digitar_salario())
            
        elif opcao == "2":
            f.criar_repositores(Sistema_principal, f.digitar_nome(), f.digitar_salario())
            
        elif opcao == "3":
            f.criar_clientes(Sistema_principal, f.digitar_nome())
            
        elif opcao == "4":
            produto = f.criar_produtos(Sistema_principal, f.digitar_nome(), f.digitar_preco(), f.digitar_quantidade())
            
            if produto != None:
                estoque = f.verificar_estoque(Sistema_principal)
                
                if estoque != None:
                    estoque.adicionar_produto(produto[0], produto[1])
                else:
                    Sistema_principal.remover_produto(produto[0])
            
        elif opcao == "5":
            f.criar_estoque(Sistema_principal, f.digitar_nome())
            
        elif opcao == "6":
            f.criar_prateleira(Sistema_principal, f.digitar_nome())
            
        elif opcao == "7":
            Estoque = f.verificar_estoque(Sistema_principal)
            
            if Estoque != None:
                Estoque.exibir_produtos_estoque()
                f.pausar_terminal()
                
        elif opcao == "8":
            Prateleira = f.verificar_prateleira(Sistema_principal)
           
            if Prateleira != None:
                print(Prateleira)
                print("\nProdutos:\n")
                Prateleira.exibir_produtos()
                f.pausar_terminal()
           
        elif opcao == "9":
            Cliente = f.verificar_cliente(Sistema_principal)
            
            if Cliente != None:
                print(Cliente)
                f.pausar_terminal()
                
        elif opcao == "10":
            Repositor = f.verificar_repositor(Sistema_principal)
            
            if Repositor != None:
                print(Repositor)
                f.pausar_terminal()
        
        elif opcao == "11":
            Gerente = f.verificar_gerente(Sistema_principal)
            
            if Gerente != None:
                print(Gerente)
                f.pausar_terminal()
            
        elif opcao == "12":
            Sistema_principal.exibir_historico_movimentacao_geral()
            f.pausar_terminal()
            
        elif opcao == "13":
            Sistema_principal.exibir_historico_compras_geral()
            f.pausar_terminal()
            
        elif opcao == "14":
            Sistema_principal.exibir_historico_vendas_geral()
            f.pausar_terminal()
            
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
            
