from datetime import datetime

#Classe Abstrata
class Pessoa:
    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade

#Herança
class Autor(Pessoa):
    pass

#Herança
class Usuario(Pessoa):
    def __init__(self, nome, telefone, nacionalidade):
        super().__init__(nome, nacionalidade)
        self.telefone = telefone


class Exemplar:
    def __init__(self, numero, edicao, emprestado=False):
        self.numero = numero
        self.edicao = edicao
        self.emprestado = emprestado


class Livro:
    def __init__(self, titulo, editora, autores, generos, exemplares, max_renovacoes=0):
        self.titulo = titulo
        self.editora = editora
        self.autores = autores
        self.generos = generos
        self.exemplares = exemplares
        self.max_renovacoes = max_renovacoes


class Emprestimo:
    def __init__(
        self,
        usuario,
        exemplar,
        data_emprestimo,
        data_devolucao=None,
        estado="emprestado",
    ):
        self.usuario = usuario
        self.exemplar = exemplar
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
        self.estado = estado


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.emprestimos = []

    #Encapsulamento
    def adicionar_livro(self, livro):
        self.livros.append(livro)

    #Encapsulamento
    def registrar_emprestimo(self, usuario, titulo_livro):
        for livro in self.livros:
            if livro.titulo == titulo_livro:
                for exemplar in livro.exemplares:
                    if not exemplar.emprestado:
                        exemplar.emprestado = True
                        emprestimo = Emprestimo(usuario, exemplar, livro,datetime.now())
                        self.emprestimos.append(emprestimo)
                        return emprestimo
        return None

    #Encapsulamento
    def devolver_exemplar(self, emprestimo):
        emprestimo.exemplar.emprestado = False
        emprestimo.data_devolucao = datetime.now()
        emprestimo.estado = "devolvido"

    #Encapsulamento
    def listar_emprestimos(self):
        return self.emprestimos


# Exemplo de uso
biblioteca = Biblioteca()

autor = Autor(nome="Luciano Ramalho", nacionalidade="Brasileiro")
exemplar = Exemplar(numero=1, edicao=2)
livro = Livro(
    titulo="Python Fluente",
    editora="O'Reilly",
    autores=[autor],
    generos=["Programação"],
    exemplares=[exemplar],
)

biblioteca.adicionar_livro(livro)

usuario = Usuario(nome="João Silva", telefone="987654321", nacionalidade="Brasileiro")
emprestimo = biblioteca.registrar_emprestimo(usuario, "Python Fluente")

print(
    f"Empréstimo realizado: {emprestimo.usuario.nome} emprestou {emprestimo.exemplar.numero} do livro {emprestimo.exemplar.edicao}"
)

biblioteca.devolver_exemplar(emprestimo)

print(
    f"Empréstimo devolvido: {emprestimo.usuario.nome} devolveu {emprestimo.exemplar.numero} do livro {emprestimo.exemplar.edicao}"
)

