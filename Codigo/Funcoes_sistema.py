import Classes as clas




def criar_gerente(sistema:clas.SISTEMA ,nome:str, salario:float):
    gerente = clas.GERENTE(nome, salario)
    sistema.adicionar_gerente(gerente)
    
    
def criar_repositores(sistema:clas.SISTEMA, nome:str, salario:float):
    repositor = clas.REPOSITOR(nome, salario)
    sistema.adicionar_repositor(repositor)
    
    
def criar_clientes(sistema:clas.SISTEMA, nome:str):
    cliente = clas.CLIENTE(nome)
    sistema.adicionar_cliente(cliente)


def criar_produtos(sistema:clas.SISTEMA, nome:str, preco:float, quantidade:int):
    produto = clas.PRODUTO(nome, preco, quantidade)
    sistema.adicionar_produto(produto)
    
def criar_estoque(sistema:clas.SISTEMA, nome:str):
    estoque = clas.ESTOQUE(nome)
    sistema.adicionar_estoque(estoque)

def criar_prateleira(sistema:clas.SISTEMA, nome:str):
    prateleira = clas.PRATELEIRA(nome)
    sistema.adicionar_prateleira(prateleira)






def retornar_pro_local_de_origem(sistema:clas.SISTEMA, produto:clas.PRODUTO, local):
    
    if type(local) == clas.ESTOQUE:
        local.adicionar_produto(produto, produto.quantidade)
        return
    
    if type(local) == clas.PRATELEIRA:
        local.adicionar_produto(produto, produto.quantidade)
        return


def inciar_sistema():
    sistema = clas.SISTEMA()
    criar_gerente(sistema, "gerente_inicial", 1500)
    return sistema