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
        
    def __str__(self):
        return f'Produto: {self._nome}, Preço: {self._preco}, Tipo: {self._tipo}'


class HISTORICO(abc.ABC):
    
    def __init__(self):
        self._historico = []
        
    @abc.abstractmethod
    def adicionar_item(self, item):
        pass
    
    def __str__(self):
        return "\n".join(self._historico)


class HISTORICO_MOVIMENTACAO():
    
    def adicionar_item(self, tipo:str, produto:PRODUTO):
        self._movimentacoes.append(f'{tipo}\n{produto.nome}')
        
    def __str__(self):
        return "\n".join(self._movimentacoes)
    
    
class HISTORICO_TRANSACOES():
    
    def adicionar_item(self, tipo:str, valor:float):
        self._transacoes.append(f'{tipo}: R${valor}')
        
        
class HISTORICO_COMPRAS():
        
    def adicionar_item(self, produto:PRODUTO, quantidade:int):
        self._compras.append(f'{produto.nome}: {quantidade}')
        
    def __str__(self):
        return "\n".join(self._compras)
        

class PRATELEIRA(IDENTIFICADOR):
    
    def __init__(self, nome:str):
        super().__init__(nome)
        self._produtos = []
        
        
    def adicionar_produto(self, produto:PRODUTO):
        
        if produto not in self._produtos:
            self._produtos.append(produto)
        
    def remover_produto(self, produto:PRODUTO):
        
        if produto in self._produtos:
            self._produtos.remove(produto)
        
    
    def adicionar_quantidade_produto(self, produto:PRODUTO, quantidade:int):
        
        if produto in self._produtos:
            if quantidade > 0:
                produto._quantidade += quantidade
        
        
    
    def retirar_quantidade_produto(self, produto: PRODUTO, quantidade:int):
        
        if produto in self._produtos:
            if quantidade > 0 and quantidade <= produto._quantidade:
                produto._quantidade -= quantidade
        
                
        
    def __str__(self):
        produtos_str = "\n".join(str(pro) for pro in self._produtos.values())
        return f'Prateleira {self._id}: {self.nome}\nProdutos:{produtos_str}\n'
    

class SACOLA_DE_COMPRAS:
    
    def __init__(self):
        # Dicionario com chave sendo o produto e valor sendo a quantidade pegada pelo cliente
        self._produtos = {}
        self._preco_total = 0.0
        
    
    def adicionar_produto(self, produto:PRODUTO, quantidade:int):
        if produto in self._produtos:
            self._produtos[produto] += quantidade
        else:
            self._produtos[produto] = quantidade
        
        self._preco_total += produto._preco * self._produtos[produto]
    
    def remover_produto(self, produto:PRODUTO, quantidade:int):
        if produto in self._produtos:
            if quantidade > 0 and quantidade <= self._produtos[produto]:
                self._produtos[produto] -= quantidade
                self._preco_total -= produto._preco * quantidade
                
            if self._produtos[produto] == 0:
                self._produtos.pop(produto)
    
    def limpar_sacola(self):
        self._produtos.clear()
        self._preco_total = 0.0
        
    def __str__(self):
        produtos_str = "\n".join(f'{pro.nome}: {quantidade}' for pro, quantidade in self._produtos.items())
        return f'Sacola de compras:\n{produtos_str}\nPreço total: R${self._preco_total}\n'
    

class CLIENTE(IDENTIFICADOR):
    
    def __init__(self, nome):
        super().__init__(nome)
        self._historico_compras = []
        self._saldo = 0.0
        self._historico_transacoes = HISTORICO_TRANSACOES()
        self.sacola = SACOLA_DE_COMPRAS()
        
    
    @property
    def saldo(self):
        return self._saldo
    
    def adicionar_saldo(self, valor:float):
        
        if valor > 0:
            self._saldo += valor
            self._historico_transacoes.append(f'Deposito de R${valor}')
            
    def remover_saldo(self, valor:float):
        
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor
            self._historico_transacoes.append(f'Saque de R${valor}')
            
            
    def __str__(self):
        return f'Cliente: {self.nome}\nID: {self._id}\nSaldo: {self._saldo}\n'


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
        if salario > 0:
            self._salario = salario
    
    def __str__(self):
        return f'Funcionário: {self.nome}\nID: {self._id}\nSalário: {self._salario}\n'


class REPOSITOR(FUNCIONARIO):
    
    def adicionar_produto_prateleira(self, prateleira:PRATELEIRA, produto:PRODUTO):
        prateleira.adicionar_produto(produto)
        self._historico_movimentacao_pessoal.adicionar_item('Adicionou produto', produto)
        
    def remover_produto_prateleira(self, prateleira:PRATELEIRA, produto:PRODUTO):
        prateleira.remover_produto(produto)
        self._historico_movimentacao_pessoal.adicionar_item('Removeu produto', produto)
        
    def adicionar_quantidade_produto_prateleira(self, prateleira:PRATELEIRA, produto:PRODUTO, quantidade:int):
        prateleira.adicionar_quantidade_produto(produto, quantidade)
        self._historico_movimentacao_pessoal.adicionar_item('Adicionou quantidade', produto)
        
    def retirar_quantidade_produto_prateleira(self, prateleira:PRATELEIRA, produto:PRODUTO, quantidade:int):
        prateleira.retirar_quantidade_produto(produto, quantidade)
        self._historico_movimentacao_pessoal.adicionar_item('Retirou quantidade', produto)
    

class GERENTE(FUNCIONARIO):
    
        
    def __str__(self):
        return f'Gerente: {self.nome}\nID: {self._id}\n'


class ESTOQUE(IDENTIFICADOR):
    
    def __init__(self, nome:str):
        super().__init__(nome)
        self._estoque = []
        self._historico_movimentacao_geral = HISTORICO_MOVIMENTACAO()
        
    def adicionar_produto(self, produto:PRODUTO):
        self._estoque.append(produto)
        self._historico_movimentacao_geral.adicionar_item('Adicionou produto', produto)
        
    def remover_produto(self, produto:PRODUTO):
        self._estoque.remove(produto)
        self._historico_movimentacao_geral.adicionar_item('Removeu produto', produto)
        
    def __str__(self):
        return "\n".join(str(pro) for pro in self._estoque)

   
class SISTEMA:
    
    def __init__(self):
        self._estoque = []
        self._prateleiras = []
        self._clientes = []
        self._funcionarios = []
        self._gerentes = []
        
    
    def criar_id():
        return random.randint(1, 999)
    
    def conferir_id(self, id:int, lista):
        for item in lista:
            if item.ID == id:
                return True
        return False
    
    def atribuir_id(self, lista):
        while True:
            id = self.atribuir_id()
            if not self.conferir_id(id, lista):
                return id
        
        
    
    def adicionar_estoque(self, estoque:ESTOQUE):
        estoque.ID = self.atribuir_id(self._estoque)
        self._estoque.append(estoque)
        
        
        
        
    def adicionar_prateleira(self, prateleira:PRATELEIRA):
        prateleira.ID = self.atribuir_id(self._prateleiras)
        self._prateleiras.append(prateleira)
        
    def adicionar_cliente(self, cliente:CLIENTE):
        cliente.ID = self.atribuir_id(self._clientes)
        self._clientes.append(cliente)
        
    def adicionar_funcionario(self, funcionario:FUNCIONARIO):
        funcionario.ID = self.atribuir_id(self._funcionarios)
        self._funcionarios.append(funcionario)
        
    def adicionar_gerente(self, gerente:GERENTE):
        gerente.ID = self.atribuir_id(self._gerentes)
        self._gerentes.append(gerente)
        
    def remover_estoque(self, estoque:ESTOQUE):
        self._estoque.remove(estoque)
    
    def remover_prateleira(self, prateleira:PRATELEIRA):
        self._prateleiras.remove(prateleira)
    
    def remover_cliente(self, cliente:CLIENTE):
        self._clientes.remove(cliente)

    def remover_funcionario(self, funcionario:FUNCIONARIO):
        self._funcionarios.remove(funcionario)

        
    
        
    
    
        
    