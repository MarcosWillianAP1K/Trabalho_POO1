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

def criar_produtos(sistema:clas.SISTEMA, nome:str, preco:float, tipagem:str):
    if nome == "" or preco <= 0:
        print("Nome, preco ou quantidade invalido")
        pausar_terminal()
        return None
    
    if len(sistema.estoques) == 0:
        print("Nenhum estoque cadastrado")
        pausar_terminal()
        return None
    
    produto = clas.PRODUTO(nome, preco, tipagem)
    sistema.adicionar_produto(produto)
    
    return produto
    
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

def digitar_unidade():
    try:
        quantidade = int(input("Digite a quantidade: "))
    except:
        return 0
    
    return quantidade

def digitar_peso():
    try:
        peso = float(input("Digite o peso: "))
    except:
        return 0
    
    return peso

def digitar_tipagem():
    while(True):
        
        print("1 - Unidade")
        print("2 - Peso")
        
        tipagem = input("Digite a tipagem: ")
        
        if tipagem == "1":
            return "Unidade"
        elif tipagem == "2":
            return "Peso"
        else:
            print("Tipagem invalida")
            pausar_terminal()
            limpar_terminal()
        
def digitar_quantidade( produto:clas.PRODUTO, quantidade:float):
    
    limpar_terminal()
    print(produto)
    if quantidade > 0:
        print("Quantidade atual: ", quantidade)
    
    if produto.tipo == "Unidade":
        return digitar_unidade()
    
    if produto.tipo == "Peso":
        return digitar_peso()

    return None


def selecionar_item(lista:list):
    while(True):
        for e in lista:
            print(e)
            print()
            
        while(True):
            try:
                id = int(input("Digite o ID do item que deseja selecionar (ou 0 para sair): "))
                break
            except:
                print("ID invalido")
        
        if id == "0":
            return None
        
        for e in lista:
            if e.ID== id:
                
                return e
            
        return "nao encontrado"

def selecionar_produto(produtos:dict):
    
     while(True):
        
        while(True):
            try:    
                id = int(input("Digite o ID do item que deseja selecionar (ou 0 para sair): ") )
                break
            except:
                print("ID invalido")
                
        if id == "0":
            return None
        
        for e in produtos:
            if e.ID == id:
                return [e, produtos[e]]
            
            
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


def verificar_sacola(sacola : clas.SACOLA_DE_PRODUTOS):
    
    if len(sacola.produtos) == 0:
        print("Nenhum produto na sacola")
        pausar_terminal()
        return None
    
    if len(sacola.produtos) == 1:
        return [list(sacola.produtos.keys())[0], list(sacola.produtos.values())[0]]
    
    while(True):
        
        print(sacola)
        
        Resultado = selecionar_item(sacola.produtos)
        
        if Resultado != "nao encontrado":
            return Resultado
            
        print("Produto nao encontrado na sacola")
        
    
def verificar_produto_estoque(estoque:clas.ESTOQUE):
    
    if len(estoque.estoque) == 0:
        print("Nenhum produto no estoque")
        pausar_terminal()
        return None
    
    if len(estoque.estoque) == 1:
        return [list(estoque.estoque.keys())[0], list(estoque.estoque.values())[0]]
    
    while(True):
        
        estoque.exibir_produtos_estoque()
        
        Resultado = selecionar_produto(estoque.estoque)
        
        if Resultado != "nao encontrado":
            return Resultado
            
        print("Produto nao encontrado no estoque")
        pausar_terminal()


def verificar_produto_prateleira(prateleira:clas.PRATELEIRA):
    
    if len(prateleira.produtos) == 0:
        print("Nenhum produto na prateleira")
        pausar_terminal()
        return None
    
    if len(prateleira.produtos) == 1:
        return [list(prateleira.produtos.keys())[0], list(prateleira.produtos.values())[0]]
    
    while(True):
        
        prateleira.exibir_produtos()
        
        Resultado = selecionar_produto(prateleira.produtos)
        
        if Resultado != "nao encontrado":
            return Resultado
            
        print("Produto nao encontrado na prateleira")
        pausar_terminal()

        
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



def retornar_pro_local_de_origem(sistema:clas.SISTEMA, produto:clas.PRODUTO, quantidade:float, local):
    
    if type(local) == clas.ESTOQUE:
        local.adicionar_produto(produto, quantidade)
        return
    
    if type(local) == clas.PRATELEIRA:
        local.adicionar_produto(produto, quantidade)
        return


def voltar_todos_para_origem(sistema: clas.SISTEMA ,sacola:clas.SACOLA_DE_PRODUTOS):
    
   for pro, lista in sacola.produtos.items():
       
       retornar_pro_local_de_origem(sistema, pro, lista[0], lista[1])
    
    



def iniciar_sistema():
    sistema = clas.SISTEMA()
    criar_gerente(sistema, "gerente_inicial", 1500)
    criar_repositores(sistema, "repositor_inicial", 1500)
    criar_clientes(sistema, "cliente_inicial")
    criar_estoque(sistema, "estoque_inicial")
    criar_prateleira(sistema, "prateleira_inicial")
    Produto = criar_produtos(sistema, "produto_inicial", 1.0, "Unidade")
    sistema.estoques[0].adicionar_produto(Produto, 10)
    
    return sistema