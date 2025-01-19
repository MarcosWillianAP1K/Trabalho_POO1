import Classes as clas


def limpar_terminal():
    
    import os
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
def pausar_terminal():
    
    import os
    
    os.system('pause' if os.name == 'nt' else 'read -p "Pressione enter para continuar"')


def criar_gerente(sistema:clas.SISTEMA ,nome:str, salario:float):
    if nome == "" or salario < 1500:
        print("Nome ou salario invalido")
        pausar_terminal()
        return
    
    gerente = clas.GERENTE(nome, salario)
    sistema.adicionar_gerente(gerente)
    
def criar_repositores(sistema:clas.SISTEMA, nome:str, salario:float):
    if nome == "" or salario < 1500:
        print("Nome ou salario invalido")
        pausar_terminal()
        return
    
    repositor = clas.REPOSITOR(nome, salario)
    sistema.adicionar_repositor(repositor)
        
def criar_clientes(sistema:clas.SISTEMA, nome:str):
    if nome == "":
        print("Nome invalido")
        pausar_terminal()
        return
    
    cliente = clas.CLIENTE(nome)
    sistema.adicionar_cliente(cliente)

def criar_produtos(sistema:clas.SISTEMA, nome:str, preco:float, quantidade:int):
    if nome == "" or preco <= 0 or quantidade <= 0:
        print("Nome, preco ou quantidade invalido")
        pausar_terminal()
        return None
    
    if len(sistema.estoques) == 0:
        print("Nenhum estoque cadastrado")
        pausar_terminal()
        return None
    
    produto = clas.PRODUTO(nome, preco, quantidade)
    sistema.adicionar_produto(produto)
    
    return [produto, quantidade]
    
def criar_estoque(sistema:clas.SISTEMA, nome:str):
    if nome == "":
        print("Nome invalido")
        pausar_terminal()
        return None
    
    estoque = clas.ESTOQUE(nome)
    sistema.adicionar_estoque(estoque)
    

def criar_prateleira(sistema:clas.SISTEMA, nome:str):
    if nome == "":
        print("Nome invalido")
        pausar_terminal()
        return
    
    prateleira = clas.PRATELEIRA(nome)
    sistema.adicionar_prateleira(prateleira)
    
    
def digitar_nome():    
    nome = input("Digite o nome: ")
    return nome

def digitar_salario():
    try:
        salario = float(input("Digite o salario: "))
    except:
        return 0
    
    return salario
    
def digitar_preco():
    try:
        preco = float(input("Digite o preco: "))
    except:
        return 0
    
    return preco

def digitar_quantidade():
    try:
        quantidade = int(input("Digite a quantidade: "))
    except:
        return 0
    
    return quantidade
    

def selecionar_item(lista:list):
    while(True):
        for e in lista:
            print(e)
            print()
            
        id = input("Digite o ID do item que deseja selecionar (ou 0 para sair): ") 
        
        if id == "0":
            return None
        
        for e in lista:
            if e.ID== id:
                
                return e
            
        return "nao encontrado"
    
    
def verificar_estoque(sistema:clas.SISTEMA):
    
    if len(sistema.estoques) == 0:
        print("Nenhum estoque cadastrado")
        return None
    
    if len(sistema.estoques) == 1:
        return sistema.estoques[0]
    
    
    while(True):
        
        sistema.exibir_estoques()
        
        Resultado = selecionar_item(sistema.estoques)
        
        if Resultado != "nao encontrado":
            return Resultado
        
        print("Estoque nao encontrado")


def verificar_prateleira(sistema:clas.SISTEMA):
    
    if len(sistema.prateleiras) == 0:
        print("Nenhuma prateleira cadastrada")
        return None
    
    if len(sistema.prateleiras) == 1:
        return sistema.prateleiras[0]
    
    
    while(True):
        
        sistema.exibir_prateleiras()
            
        Resultado = selecionar_item(sistema.prateleiras)
        
        if Resultado != "nao encontrado":
            return Resultado
            
        print("Prateleira nao encontrada")
        
        
def verificar_cliente(sistema:clas.SISTEMA):
    
    if len(sistema.clientes) == 0:
        print("Nenhum cliente cadastrado")
        return None
    
    if len(sistema.clientes) == 1:
        return sistema.clientes[0]
    
    
    while(True):
       
        sistema.exibir_clientes()
        
        Resultado = selecionar_item(sistema.clientes)
        
        if Resultado != "nao encontrado":
            return Resultado
            
        print("Cliente nao encontrado")
        
        
def verificar_gerente(sistema:clas.SISTEMA):
    
    if len(sistema.gerentes) == 0:
        print("Nenhum gerente cadastrado")
        return None
    
    if len(sistema.gerentes) == 1:
        return sistema.gerentes[0]
    
    
    while(True):
        
        sistema.exibir_gerentes()
        
        Resultado = selecionar_item(sistema.gerentes)
        
        if Resultado != "nao encontrado":
            return Resultado
            
        print("Gerente nao encontrado")
    
    
def verificar_repositor(sistema:clas.SISTEMA):
    
    if len(sistema.repositores) == 0:
        print("Nenhum repositor cadastrado")
        return None
    
    if len(sistema.repositores) == 1:
        return sistema.repositores[0]
    
    
    while(True):
        
        sistema.exibir_repositores()
        
        Resultado = selecionar_item(sistema.repositores)
        
        if Resultado != "nao encontrado":
            return Resultado
            
        print("Repositor nao encontrado")
        
        
def verificar_historico_movimentacao_geral(sistema:clas.SISTEMA):
    
    sistema.exibir_historico_movimentacao_geral()


def verificar_historico_compras_geral(sistema:clas.SISTEMA):
    
    sistema.exibir_historico_compras_geral()
        

def verificar_historico_vendas_geral(sistema:clas.SISTEMA):
    
    sistema.exibir_historico_vendas_geral()


def exibir_conteudo_da_lista(lista:list):
    
    for e in lista:
        print(e)
        print()



def retornar_pro_local_de_origem(sistema:clas.SISTEMA, produto:clas.PRODUTO, local):
    
    if type(local) == clas.ESTOQUE:
        local.adicionar_produto(produto, produto.quantidade)
        return
    
    if type(local) == clas.PRATELEIRA:
        local.adicionar_produto(produto, produto.quantidade)
        return


def iniciar_sistema():
    sistema = clas.SISTEMA()
    criar_gerente(sistema, "gerente_inicial", 1500)
    criar_repositores(sistema, "repositor_inicial", 1500)
    criar_clientes(sistema, "cliente_inicial")
    criar_estoque(sistema, "estoque_inicial")
    criar_prateleira(sistema, "prateleira_inicial")
    Produto = criar_produtos(sistema, "produto_inicial", 1.0, 1)
    sistema.estoques[0].adicionar_produto(Produto[0], Produto[1])
    
    return sistema