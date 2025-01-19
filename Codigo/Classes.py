import abc
import random


class IDENTIFICADOR(abc.ABC):
    
    def __init__(self, nome:str):
        self._id = 0
        self.nome = nome
        
        
    @property
    def ID(self):
        return self._id
    
    @ID.setter
    def ID(self, id:int):
        if id > 0:
            self._id = id
            
    
    @abc.abstractmethod
    def __str__(self):
        pass


class PRODUTO(IDENTIFICADOR):
    
    def __init__(self, nome:str, preco:float, tipo:str):
        super().__init__(nome)
        self._preco = preco
        self._tipo = tipo
        
    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, preco:float):
        if preco > 0:
            self._preco = preco
            
    @property
    def tipo(self):
        return self._tipo
    
    @tipo.setter
    def tipo(self, tipo:str):
        self._tipo = tipo
        
    def __str__(self):
        return f'ID: {self.ID:03}\nProduto: {self.nome}\nPreço: {self.preco}\nTipo: {self.tipo}'


class HISTORICO(abc.ABC):
    
    def __init__(self):
        self._historico = []
        
    @property
    def historico(self):
        return self._historico
    
    @historico.setter
    def historico(self, historico:list):
        self._historico = historico
        
    @abc.abstractmethod
    def adicionar_item(self, item):
        pass
    
    def __iter__(self):
        return iter(self.historico)  # Torna o histórico iterável
    
    def __str__(self):
        return "\n\n".join(item for item in self.historico)


class HISTORICO_MOVIMENTACAO(HISTORICO):
    
    def adicionar_item(self, tipo:str, produto:PRODUTO):
        self.historico.append(f'{tipo}:\n{str(produto)}')
        
    
    
class HISTORICO_TRANSACOES(HISTORICO):
    
    def adicionar_item(self, tipo:str, valor:float):
        self.historico.append(f'{tipo}: R${valor}')
        
        
class HISTORICO_COMPRAS(HISTORICO):
        
    def adicionar_item(self, produto:PRODUTO, quantidade:int):
        self.historico.append(f'ID: {produto.ID}\nProduto: {produto.nome}\nQuantidade: {quantidade}\nValor: R${produto._preco * quantidade}\n')
        
    
        

class PRATELEIRA(IDENTIFICADOR):
    
    def __init__(self, nome:str):
        super().__init__(nome)
        self._produtos = {}
        
    @property
    def produtos(self):
        return self._produtos
        
        
    def adicionar_produto(self, produto:PRODUTO, quantidade:float):
        
        if produto not in self.produtos:
            self.produtos[produto] = quantidade
        else:
            self.produtos[produto] += quantidade
        
        
    def retirar_produto(self, produto:PRODUTO, quantidade:float):
        
        if produto in self.produtos:
            if quantidade > 0 and quantidade <= self.produtos[produto]:
                self.produtos[produto] -= quantidade
                
            if self.produtos[produto] == 0:
                self.produtos.pop(produto)
            
    def remover_todos_produto(self, produto:PRODUTO):
        self.produtos.pop(produto)
        
    def esvaziar_prateleira(self):
        self.produtos.clear()
            
    def exibir_produtos(self):
        for produto, quantidade in self.produtos.items():
            print(f'{produto}\nQuantidade: {quantidade}\n')
                
        
    def __str__(self):
        return f'Prateleira {self.ID}: {self.nome}'
    

class SACOLA_DE_PRODUTOS:
    
    def __init__(self):
        # Dicionario com chave sendo o produto e valor sendo a quantidade pegada pelo cliente
        self._produtos = {}
        self._preco_total = 0.0
    
    
    @property
    def produtos(self):
        return self._produtos
    
    @property
    def preco_total(self):
        return self._preco_total
    
    @preco_total.setter
    def preco_total(self, preco:float):
        if preco >= 0:
            self._preco_total = preco
        else :
            self._preco_total = 0.0
    
    
    def adicionar_produto(self, produto:PRODUTO, quantidade:float, local_origem):
        if produto in self._produtos:
            self.produtos[produto][0] += quantidade
        else:
            self.produtos[produto] = [quantidade, local_origem]
        
        self.preco_total = (self.preco_total + (produto.preco * quantidade))
    
    def remover_produto(self, produto:PRODUTO, quantidade:float):
        if produto in self._produtos:
            if quantidade > 0 and quantidade <= self._produtos[produto][0]:
                self.produtos[produto][0] -= quantidade
                self.preco_total = (self.preco_total - (produto.preco * quantidade))
                
            if self.produtos[produto][0] == 0:
                self.produtos.pop(produto)
        
    
    def limpar_sacola(self):
        self.produtos.clear()
        self.preco_total = 0.0
        
    def __str__(self):
        produtos_str = "\n\n".join(f'{pro}\nQuantidade: {quantidade[0]}' for pro, quantidade in self._produtos.items())
        return f'Sacola:\n{produtos_str}\n\nPreço total: R${self._preco_total}\n\n'
    

class CLIENTE(IDENTIFICADOR):
    
    def __init__(self, nome):
        super().__init__(nome)
        self._historico_compras = []
        self._saldo = 0.0
        self._historico_transacoes = HISTORICO_TRANSACOES()
        self._sacola = SACOLA_DE_PRODUTOS()
        
    
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, saldo:float):
        if saldo >= 0:
            self._saldo = saldo
        else:
            self._saldo = 0.0
    
    @property
    def sacola(self):
        return self._sacola
    
    @property
    def historico_compras(self):
        return self._historico_compras
    
    @property
    def historico_transacoes(self):
        return self._historico_transacoes
    
    def finalizar_compra(self):
        if self.sacola.preco_total <= self._saldo:
            self.historico_compras.append(str(self.sacola))
            self.saldo = (self.saldo - self.sacola.preco_total)
            self.sacola.limpar_sacola()
        
    def adicionar_saldo(self, valor:float):
        
        if valor > 0:
            self.saldo = (self.saldo + valor)
            self.historico_transacoes.adicionar_item('Depósito', valor)
            
    def remover_saldo(self, valor:float):
        
        if valor > 0 and valor <= self._saldo:
            self.saldo = (self.saldo - valor)
            self.historico_transacoes.adicionar_item('Saque', valor)
    

    def __str__(self):
        return f'Cliente: {self.nome}\nID: {self.ID}\nSaldo: {self.saldo}'


class FUNCIONARIO(IDENTIFICADOR):
    
    def __init__(self, nome:str, salario:float):
        super().__init__(nome)
        self._salario = salario
        self._historico_movimentacao_pessoal = HISTORICO_MOVIMENTACAO()
        
    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, salario:float):
        if salario >= 1500:
            self._salario = salario
            
    @property
    def historico_movimentacao_pessoal(self):
        return self._historico_movimentacao_pessoal
    
    
    def __str__(self):
        return f'Funcionário: {self.nome}\nID: {self.ID}\nSalário: R${self.salario}'


class REPOSITOR(FUNCIONARIO):
    
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
        self._sacola = SACOLA_DE_PRODUTOS()
        
    @property
    def sacola(self):
        return self._sacola
    
    
    def adicionar_historico_movimentacao_pessoal(self, tipo:str, produto:PRODUTO, quantidade:int, local):
        self.historico_movimentacao_pessoal.adicionar_item(f'{tipo}: {quantidade}\nEm: {str(local)}', produto)
    
        
    
    def __str__(self):
        return f'Repositor: {self.nome}\nID: {self._id}'
    

class GERENTE(FUNCIONARIO):
    
        
    def __str__(self):
        return f'Gerente: {self.nome}\nID: {self._id}'


class ESTOQUE(IDENTIFICADOR):
    
    def __init__(self, nome:str):
        super().__init__(nome)
        self._estoque = {}
        self._historico_movimentacao_estoque = HISTORICO_MOVIMENTACAO()
        
    @property
    def estoque(self):
        return self._estoque
    
    @property
    def historico_movimentacao_estoque(self):
        return self._historico_movimentacao_estoque
        
    def adicionar_produto(self, produto:PRODUTO, quantidade:float):
        
        if produto not in self.estoque:
            self.estoque[produto] = quantidade
        else:
            self.estoque[produto] += quantidade
           
        self.historico_movimentacao_estoque.adicionar_item(f'Adicionou {quantidade} produto', produto)
        
    def pegar_produto(self, produto:PRODUTO, quantidade:float):
        
        if produto in self.estoque:
            if quantidade > 0 and quantidade <= self.estoque[produto]:
                self.estoque[produto] -= quantidade
                self.historico_movimentacao_estoque.adicionar_item(f'Removeu {quantidade} produto', produto)
                
            if self.estoque[produto] == 0:
                self.estoque.pop(produto)
                
    
    def exibir_produtos_estoque(self):
        for produto, quantidade in self.estoque.items():
            print(f'{produto}\nQuantidade: {quantidade}\n')
        
        
        
    def __str__(self):
        return f'Estoque {self.ID}: {self.nome}'

   
class SISTEMA:
    
    def __init__(self):
        self._estoques = []
        self._prateleiras = []
        self._clientes = []
        self._repositores = []
        self._gerentes = []
        self._produtos = []
        self._historico_vendas_geral = []
        self._historico_compras_geral = []
        self._historico_movimentacao_geral = []
        
        
        
        
        
    @property
    def estoques(self):
        return self._estoques
    
    
    @property
    def prateleiras(self):
        return self._prateleiras
    
    @property
    def clientes(self):
        return self._clientes
    
    @property
    def repositores(self):
        return self._repositores
    
    @property
    def gerentes(self):
        return self._gerentes
    
    @property
    def produtos(self):
        return self._produtos
    
    @property
    def historico_vendas_geral(self):
        return self._historico_vendas_geral
    
    @property
    def historico_compras_geral(self):
        return self._historico_compras_geral
    
    @property
    def historico_movimentacao_geral(self):
        return self._historico_movimentacao_geral
    
    
    
    def exibir_historico_vendas_geral(self):
        for venda in self._historico_vendas_geral:
            print(venda, end='\n\n')
            
    def exibir_historico_compras_geral(self):
        for compra in self.historico_compras_geral:
            print(compra, end='\n\n')
            
    def exibir_historico_movimentacao_geral(self):
        for movimentacao in self.historico_movimentacao_geral:
            print(movimentacao, end='\n\n')
            
    def exibir_gerentes(self):
        for gerente in self.gerentes:
            print(gerente, end='\n\n')
            
    def exibir_repositores(self):
        for repositor in self.repositores:
            print(repositor, end='\n\n')
            
    def exibir_clientes(self):
        for cliente in self.clientes:
            print(cliente, end='\n\n')
            
    def exibir_prateleiras(self):
        for prateleira in self.prateleiras:
            print(prateleira, end='\n\n')
            
    def exibir_estoques(self):
        for estoque in self.estoques:
            print(estoque, end='\n\n')
            
    def exibir_produtos(self):
        for produto in self.produtos:
            print(produto, end='\n\n')
            
    
        
        
    
    def criar_id(self):
        return random.randint(1, 999)
    
    def conferir_id(self, id:int, lista):
        for item in lista:
            if item.ID == id:
                return True
        return False
    
    def atribuir_id(self, lista):
        while True:
            id = self.criar_id()
            if not self.conferir_id(id, lista):
                return id
        
        
    
    def adicionar_estoque(self, estoque:ESTOQUE):
        estoque.ID = self.atribuir_id(self.estoques)
        self.estoques.append(estoque)
        
    def adicionar_prateleira(self, prateleira:PRATELEIRA):
        prateleira.ID = self.atribuir_id(self.prateleiras)
        self.prateleiras.append(prateleira)
        
    def adicionar_cliente(self, cliente:CLIENTE):
        cliente.ID = self.atribuir_id(self.clientes)
        self.clientes.append(cliente)
        
    def adicionar_repositor(self, repositor:REPOSITOR):
        repositor.ID = self.atribuir_id(self.repositores)
        self.repositores.append(repositor)
        
    def adicionar_gerente(self, gerente:GERENTE):
        gerente.ID = self.atribuir_id(self.gerentes)
        self.gerentes.append(gerente)
        
    def adicionar_produto(self, produto:PRODUTO):
        produto.ID = self.atribuir_id(self.produtos)
        self.produtos.append(produto)
        
    def adicionar_venda(self, cliente:CLIENTE, sacola:SACOLA_DE_PRODUTOS):
        self.historico_vendas_geral.append(f"Venda para {cliente}\n{sacola}")
    
    def adicionar_compra(self, gerente:GERENTE, produto:PRODUTO, quantidade:int):
        self.historico_compras_geral.append(f"Compra de {quantidade} {produto} por {gerente.nome}")
    
    def adicionar_movimentacao_geral(self, fulano, local ,tipo:str, produto:PRODUTO, quantidade:int):
        self.historico_movimentacao_geral.append(f"{tipo}: {quantidade}\n{str(produto)}\nEm: {local}\nPor: {fulano}")
        
        
    def remover_gerente(self, gerente:GERENTE):
        self.gerentes.remove(gerente)    
        
    def remover_estoque(self, estoque:ESTOQUE):
        self.estoques.remove(estoque)
    
    def remover_prateleira(self, prateleira:PRATELEIRA):
        self.prateleiras.remove(prateleira)
    
    def remover_cliente(self, cliente:CLIENTE):
        self.clientes.remove(cliente)

    def remover_repositor(self, repositor:REPOSITOR):
        self.repositores.remove(repositor)
        
    def remover_produto(self, produto:PRODUTO):
        self.produtos.remove(produto)

    