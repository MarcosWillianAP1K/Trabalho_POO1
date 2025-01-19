import Funcoes_sistema as f


def menu_sacola(Sistema_principal: f.clas.SISTEMA, sacola: f.clas.SACOLA_DE_PRODUTOS):
    
    if sacola == None or sacola.produtos == {}:
        print("Nenhum produto na sacola")
        f.pausar_terminal()
        return
    
    while(True):
        
        if sacola.produtos == {}:
            break
        
        f.limpar_terminal()
        
        print("Bem vindo a sacola")
        print("Selecione uma opcao:")
        print("1 - remover produto")
        print("2 - esvaziar sacola")
        print("3 - ver produtos")
        print("0 - Voltar")
        
        opcao = str(input("Digite a opcao desejada: "))
        
        f.limpar_terminal()
        
        if opcao == "1":
            produto = f.verificar_sacola(sacola)
            
            if produto != None:
                
                quantidade = f.digitar_quantidade(produto[0], produto[1][0])
                
                if quantidade != None and quantidade > 0:
                    sacola.remover_produto(produto[0], quantidade)
                    f.retornar_pro_local_de_origem(Sistema_principal, produto[0], quantidade, produto[1][1])
                
        
        elif opcao == "2":
            if sacola.produtos != {}:
                f.voltar_todos_para_origem(Sistema_principal, sacola)
                sacola.limpar_sacola()
                
                
        elif opcao == "3":
            print(sacola)
            f.pausar_terminal()
            
        elif opcao == "0":
            break
        
        else:
            print("Opcao invalida")
            f.pausar_terminal()
       




def menu_cliente(Sistema_principal: f.clas.SISTEMA, cliente:f.clas.CLIENTE):
    
    if cliente == None or Sistema_principal == None:
        print("Nenhum cliente cadastrado")
        f.pausar_terminal()
        return
    
    while(True):
        f.limpar_terminal()
        
        print(f"Bem vindo cliente {cliente.nome}")
        print("Saldo: R$", cliente.saldo)
        print("Selecione uma opcao:")
        print("1 - Ver prateleiras")
        print("2 - Ver sacola")
        print("3 - Finalizar compra")
        print("4 - Adicionar saldo")
        print("5 - Remover saldo")
        print("6 - Ver historico de compras")
        print("7 - Ver historico de transacoes")
        print("0 - Voltar")
        
        opcao = str(input("Digite a opcao desejada: "))
        
        f.limpar_terminal()
        
        if opcao == "1":
            prateleira = f.verificar_prateleira(Sistema_principal)
            
            if prateleira != None:
                produto = f.verificar_produto_prateleira(prateleira)
            
                if produto != None:
                    quantidade = f.digitar_quantidade(produto[0], produto[1])
                    
                    if quantidade != None and quantidade > 0:
                        cliente.sacola.adicionar_produto(produto[0], quantidade, prateleira)
                        prateleira.retirar_produto(produto[0], quantidade)
                        Sistema_principal.adicionar_movimentacao_geral(str(cliente), prateleira ,"Adicionou",produto[0], quantidade)
        elif opcao == "2":
            menu_sacola(Sistema_principal, cliente.sacola)
            
        elif opcao == "3":
            f.finalizar_compra(Sistema_principal, cliente)
        elif opcao == "4":
            cliente.adicionar_saldo(f.digitar_saldo())
        elif opcao == "5":
            cliente.remover_saldo(f.digitar_saldo())
        elif opcao == "6":
            print(cliente.historico_compras)
            f.pausar_terminal()
        elif opcao == "7":
            print(cliente.historico_transacoes.historico)
            f.pausar_terminal()
        elif opcao == "0":
            break
        else:
            print("Opcao invalida")
            f.pausar_terminal()


def menu_prateleira_repositor(Sistema_principal: f.clas.SISTEMA, repositor:f.clas.REPOSITOR, prateleira:f.clas.PRATELEIRA):
    
    if prateleira == None:
        print("Nenhuma prateleira cadastrada")
        f.pausar_terminal()
        return
    
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
                quantidade = f.digitar_quantidade(produto[0], produto[1][0])
                
                if quantidade != None and quantidade > 0:
                
                    prateleira.adicionar_produto(produto[0], quantidade)
                    repositor.sacola.remover_produto(produto[0], quantidade)
                    repositor.adicionar_historico_movimentacao_pessoal("Adicionou", produto[0], quantidade, prateleira)
                    Sistema_principal.adicionar_movimentacao_geral(str(repositor), prateleira ,"Adicionou",produto[0], quantidade)
        
        elif opcao == "2":
            produto = f.verificar_produto_prateleira(prateleira)
            
            if produto != None:
                quantidade = f.digitar_quantidade(produto[0], produto[1][0])
                
                if quantidade != None and quantidade > 0:
                
                    repositor.sacola.adicionar_produto(produto[0], quantidade, prateleira)
                    prateleira.pegar_produto(produto[0], quantidade)
                    repositor.adicionar_historico_movimentacao_pessoal("Retirou", produto[0], quantidade, prateleira)
                    Sistema_principal.adicionar_movimentacao_geral(str(repositor), prateleira ,"Retirou",produto[0], quantidade)
        
        elif opcao == "3":
            prateleira.exibir_produtos()
            f.pausar_terminal()
            
        elif opcao == "0":
            break
        else:
            print("Opcao invalida")
            f.pausar_terminal()
    
    
def menu_estoque(Sistema_principal: f.clas.SISTEMA, repositor:f.clas.REPOSITOR ,estoque:f.clas.ESTOQUE):
    
    if  estoque == None:
        print("Nenhum estoque cadastrado")
        f.pausar_terminal()
        return
    
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
                quantidade = f.digitar_quantidade(produto[0], produto[1][0])
                
                if quantidade != None and quantidade > 0:
                    estoque.adicionar_produto(produto[0], quantidade)
                    repositor.sacola.remover_produto(produto[0], quantidade)
                    repositor.adicionar_historico_movimentacao_pessoal("Adicionou", produto[0], quantidade, estoque)
                    Sistema_principal.adicionar_movimentacao_geral(str(repositor), estoque ,"Adicionou",produto[0], quantidade)
        
        elif opcao == "2":
            produto = f.verificar_produto_estoque(estoque)
            
            if produto != None:
                quantidade = f.digitar_quantidade(produto[0], produto[1])
                
                if quantidade != None and quantidade > 0:
                    repositor.sacola.adicionar_produto(produto[0], quantidade, estoque)
                    estoque.pegar_produto(produto[0], quantidade)
                    repositor.adicionar_historico_movimentacao_pessoal("Retirou", produto[0], quantidade, estoque)
                    Sistema_principal.adicionar_movimentacao_geral(str(repositor), estoque ,"Retirou",produto[0], quantidade)
            
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
            Estoque = f.verificar_estoque(Sistema_principal)
            
            if Estoque != None:
                
                produto = f.criar_produtos(Sistema_principal, f.digitar_nome(), f.digitar_preco(), f.digitar_tipagem())
                
                if produto != None:
                    quantidade = f.digitar_quantidade(produto, 0)
                    if quantidade != None and quantidade > 0:
                        Estoque.adicionar_produto(produto, quantidade)
                        Sistema_principal.adicionar_movimentacao_geral(str(gerente), Estoque ,"Adicionou",produto, quantidade)
                        Sistema_principal.adicionar_compra(gerente ,produto, quantidade)

                    else:
                        print("Quantidade invalida")
                        Sistema_principal.remover_produto(produto)
                        f.pausar_terminal()
                   
            
            
            
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
            
