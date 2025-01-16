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

testes_adicionar_produto()