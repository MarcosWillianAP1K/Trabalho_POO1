import Classes as c


def testes_iniciar_classes():
    teste = c.SISTEMA()
    teste = c.ESTOQUE("teste")
    teste = c.PRATELEIRA("teste")
    teste = c.CLIENTE("teste")
    teste = c.FUNCIONARIO("teste", 1500)
    teste = c.GERENTE("teste", 1500)
    teste = c.PRODUTO("teste", 15, "teste")
    teste = c.REPOSITOR("teste", 1500)
    

# testes_iniciar_classes()



def testes_adicionar_produto():
    estoque = c.ESTOQUE("teste")
    produto = c.PRODUTO("teste", 15, "teste")
    estoque.adicionar_produto(produto)
    sistema = c.SISTEMA()
    sistema.adicionar_estoque(estoque)
    
    print(estoque.estoque)
    print()
    print(estoque.historico_movimentacao_geral)
    print()
    print(estoque)

# testes_adicionar_produto()




def teste_sistema():
    import Classes as c
    
    sistema = c.SISTEMA()
    estoque = c.ESTOQUE("teste")
    prateleira = c.PRATELEIRA("teste")
    cliente = c.CLIENTE("teste")
    gerente = c.GERENTE("teste", 1500)
    repositor = c.REPOSITOR("teste", 1500)
    produto = c.PRODUTO("teste", 15, "teste")
    
    cliente.adicionar_saldo
    
    sistema.adicionar_estoque(estoque)
    sistema.adicionar_prateleira(prateleira)
    sistema.adicionar_cliente(cliente)
    sistema.adicionar_gerente(gerente)
    sistema.adicionar_repositor(repositor)
    sistema.adicionar_produto(produto)
    
    # sistema.remover_estoque(estoque)
    # sistema.remover_prateleira(prateleira)
    # sistema.remover_cliente(cliente)
    # sistema.remover_gerente(gerente)
    # sistema.remover_repositor(repositor)
    

    sistema.estoques[0].adicionar_produto(produto, 10)
    sistema.repositores[0].adicionar_produto_prateleira(sistema.prateleiras[0], produto, 10)

    sistema.clientes[0].adicionar_saldo(100)
    sistema.clientes[0].remover_saldo(50)
    
    for e in sistema.estoques:
        print(e)
        for p in e.historico_movimentacao_estoque:
            print(p)
    print()
    
    for p in sistema.prateleiras:
        print(p)
        p.exibir_produtos()
    print()
    
    for c in sistema.clientes:
        print(c)
        print(c.historico_transacoes)
    print()
    
    for f in sistema.repositores:
        print(f)
        for p in f.historico_movimentacao_pessoal:
            print(p)
        
    print()
    
    for g in sistema.gerentes:
        print(g)
    print()

    
teste_sistema()

