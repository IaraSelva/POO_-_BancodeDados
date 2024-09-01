from datetime import datetime

#Classe Abstrata
class Pessoa:
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco

# -- Herança
class Fornecedor(Pessoa):
    pass

# -- Herança
class Cliente(Pessoa):
    pass


class Produto:
    def __init__(self, nome, categorias, quantidade_estoque, fornecedores):
        self.nome = nome
        self.categorias = categorias
        self.quantidade_estoque = quantidade_estoque
        self.fornecedores = fornecedores

    def reduzir_estoque(self, quantidade):
        if quantidade <= self.quantidade_estoque:
            self.quantidade_estoque -= quantidade
            return True
        return False


class Transacao:
    def __init__(self, cliente, produto, data_compra, quantidade):
        self.cliente = cliente
        self.produto = produto
        self.data_compra = data_compra
        self.quantidade = quantidade


class Mercado:
    def __init__(self):
        self.produtos = []
        self.transacoes = []

    #Encapsulamento
    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    #Encapsulamento
    def registrar_compra(self, cliente, nome_produto, quantidade):
        for produto in self.produtos:
            if produto.nome == nome_produto:
                if produto.reduzir_estoque(quantidade):
                    transacao = Transacao(cliente, produto, datetime.now(), quantidade)
                    self.transacoes.append(transacao)
                    return transacao
        return None

    #Encapsulamento
    def listar_transacoes(self):
        return self.transacoes


# Exemplo de uso
mercado = Mercado()

fornecedor = Fornecedor(
    nome="Fornecedor A", telefone="123456789", endereco="Rua A, 123"
)
produto = Produto(
    nome="Arroz",
    categorias=["Alimento", "Grãos"],
    quantidade_estoque=100,
    fornecedores=[fornecedor],
)

mercado.adicionar_produto(produto)

cliente = Cliente(nome="Maria Silva", telefone="987654321", endereco="Rua B, 456")
transacao = mercado.registrar_compra(cliente, "Arroz", 5)

print(
    f"Compra realizada: {transacao.cliente.nome} comprou {transacao.quantidade} unidades de {transacao.produto.nome}"
)

print("Transações registradas:")
for transacao in mercado.listar_transacoes():
    print(
        f"{transacao.data_compra}: {transacao.cliente.nome} comprou {transacao.quantidade} unidades de {transacao.produto.nome}"
    )
