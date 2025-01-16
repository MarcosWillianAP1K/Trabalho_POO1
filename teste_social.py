import uuid

# Classe base Pessoa
class Pessoa:
    def __init__(self, nome):
        self.id = str(uuid.uuid4())  # Gera um ID único
        self.nome = nome

    def get_id(self):
        return self.id

# Classe Repositor
class Repositor(Pessoa):
    def __init__(self, nome, salario):
        super().__init__(nome)
        self.salario = salario
        self.historico_retirada_pessoal = []  # Histórico de movimentações do repositor

    def registrar_movimentacao(self, produto, quantidade, acao):
        entrada = {
            "produto": produto,
            "quantidade": quantidade,
            "acao": acao,  # "entrada" ou "retirada"
        }
        self.historico_retirada_pessoal.append(entrada)

# Classe Cliente
class Cliente(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)
        self.carteira = 0
        self.cesta_compras = []
        self.historico_transacoes = []  # Histórico de movimentação na carteira
        self.historico_compras = []

    def depositar(self, valor):
        self.carteira += valor
        self.historico_transacoes.append({"tipo": "deposito", "valor": valor})

    def sacar(self, valor):
        if valor > self.carteira:
            raise ValueError("Saldo insuficiente.")
        self.carteira -= valor
        self.historico_transacoes.append({"tipo": "saque", "valor": valor})

    def adicionar_na_cesta(self, produto, quantidade):
        self.cesta_compras.append({"produto": produto, "quantidade": quantidade})

    def finalizar_compra(self):
        total_itens = sum(item["quantidade"] for item in self.cesta_compras)
        self.historico_compras.append({"itens": self.cesta_compras})
        self.cesta_compras = []
        return total_itens

# Classe Gerente
class Gerente(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)
        self.historico_vendas = []
        self.historico_movimentacoes_estoque = []
        self.historico_trabalhadores = []

    def contratar_repositor(self, nome, salario):
        repositor = Repositor(nome, salario)
        self.historico_trabalhadores.append({"acao": "contrato", "nome": nome})
        return repositor

    def demitir_repositor(self, repositor):
        self.historico_trabalhadores.append({"acao": "demissao", "nome": repositor.nome})

    def registrar_venda(self, venda):
        self.historico_vendas.append(venda)

    def registrar_movimentacao_estoque(self, movimentacao):
        self.historico_movimentacoes_estoque.append(movimentacao)

# Sistema de Estoque e Prateleiras
class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, produto, quantidade):
        if produto in self.produtos:
            self.produtos[produto] += quantidade
        else:
            self.produtos[produto] = quantidade

    def retirar_produto(self, produto, quantidade):
        if produto not in self.produtos or self.produtos[produto] < quantidade:
            raise ValueError("Quantidade insuficiente em estoque.")
        self.produtos[produto] -= quantidade

class Prateleiras:
    def __init__(self):
        self.prateleiras = {}

    def adicionar_prateleira(self, nome):
        if nome not in self.prateleiras:
            self.prateleiras[nome] = {}

    def organizar_produto(self, nome_prateleira, produto, quantidade):
        if nome_prateleira not in self.prateleiras:
            raise ValueError("Prateleira inexistente.")
        if produto in self.prateleiras[nome_prateleira]:
            self.prateleiras[nome_prateleira][produto] += quantidade
        else:
            self.prateleiras[nome_prateleira][produto] = quantidade

# Exemplo de uso
estoque = Estoque()
prateleiras = Prateleiras()
gerente = Gerente("Maria")

# Gerente contrata repositor
repositor = gerente.contratar_repositor("João", 1500)

# Repositor organiza estoque
estoque.adicionar_produto("Arroz", 50)
repositor.registrar_movimentacao("Arroz", 50, "entrada")

# Cliente faz compras
cliente = Cliente("Ana")
cliente.depositar(100)
cliente.adicionar_na_cesta("Arroz", 2)

# Finaliza a compra
gerente.registrar_venda(cliente.finalizar_compra())
print("Sistema de estoque e compras criado com sucesso!")
