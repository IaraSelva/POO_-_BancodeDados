from datetime import datetime, timedelta

# Classe Abstrata
class Pessoa:
    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade
    
    def __repr__(self) -> str:
        return f"{{nome: {self.nome}, nacionalidade: {self.nacionalidade}}}"

# Herança
class Autor(Pessoa):
    def __repr__(self) -> str:
        return f"{{autor = {super().__repr__()}}}"

# Herança
class Usuario(Pessoa):
    def __init__(self, nome, telefone, nacionalidade):
        super().__init__(nome, nacionalidade)
        self.telefone = telefone
    
    def __repr__(self) -> str:
        return f"{{usuario = {super().__repr__()}, telefone: {self.telefone}}}"


class Exemplar:
    def __init__(self, numero, edicao, emprestado=False):
        self.numero = numero
        self.edicao = edicao
        self.emprestado = emprestado
    
    def __repr__(self) -> str:
        return f"numero: {self.numero}, edicao: {self.edicao}, emprestado: {self.emprestado}"


class Livro:
    def __init__(self, titulo, editora, autores, genero, exemplar):
        self.titulo = titulo
        self.editora = editora
        self.autores = autores
        self.genero = genero
        self.exemplares = [exemplar]
    
    def __repr__(self) -> str:
        return f"titulo: {self.titulo}, editora: {self.editora}, autores: {self.autores}, genero: {self.genero}, exemplares: {self.exemplares}"


class Emprestimo:
    def __init__(
        self,
        usuario,
        titulo,
        exemplar,
        data_emprestimo,
        data_devolucao,
        situacao="emprestado",
    ):
        self.usuario = usuario
        self.titulo = titulo
        self.exemplar = exemplar
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
        self.situacao = situacao
    
    def __repr__(self) -> str:
        return f"emprestado para: {self.usuario}, titulo: {self.titulo}, exemplar: {self.exemplar}, data_emprestimo: {self.data_emprestimo}, data_devolucao: {self.data_devolucao}, situacao: {self.situacao}"


class Biblioteca:
    def __init__(self):
        self.livros = {}
        self.usuarios = []
        self.emprestimos = []

    # Encapsulamento
    def cadastrar_usuario(self, nome, nacionalidade, telefone):
        novo_usuario = Usuario(nome=nome, nacionalidade=nacionalidade, telefone=telefone)
        self.usuarios.append(novo_usuario)
        return novo_usuario

    # Encapsulamento
    def cadastrar_autor(self, nome, nacionalidade):
        novo_autor = Autor(nome, nacionalidade)
        return novo_autor

    # Encapsulamento
    def cadastrar_livro(self, titulo, editora, numero, edicao, autores, genero):
        exemplar = Exemplar(numero, edicao)

        if titulo in self.livros: # {"as cronics de narnia": demais infos}
            self.livros[titulo].exemplares.append(exemplar)
        else:
            novo_livro = Livro(titulo, editora, autores, genero, exemplar)
            self.livros[titulo] = novo_livro

    # Encapsulamento
    def registrar_emprestimo(self, usuario, titulo_livro):
        if titulo_livro in self.livros:
            livro = self.livros[titulo_livro]
            for exemplar in livro.exemplares:
                if not exemplar.emprestado:
                    exemplar.emprestado = True
                    emprestimo = Emprestimo(usuario, titulo_livro, exemplar, formatar_data(datetime.now()), definir_data_devolucao(7))
                    self.emprestimos.append(emprestimo)
                    return emprestimo
        return "Livro não disponível"

    # Encapsulamento
    def devolver_exemplar(self, emprestimo):           
        emprestimo.exemplar.emprestado = False
        emprestimo.data_devolucao = formatar_data(datetime.now())
        emprestimo.situacao = "devolvido"

    # Encapsulamento
    def listar_emprestimos(self):
        print(self.emprestimos)
    
    # Encapsulamento
    def listar_livros(self):
        print(self.livros)

    # Encapsulamento
    def listar_usuarios(self):
        print(self.usuarios)


# Funções auxiliares
def formatar_data(data):
    return data.strftime("%d-%m-%Y")

def definir_data_devolucao(dias_emprestados):
    return formatar_data(datetime.now() + timedelta(days = dias_emprestados))

# Exemplo de uso
biblioteca = Biblioteca()

autor = biblioteca.cadastrar_autor(nome="Luciano Ramalho", nacionalidade="Brasileiro")

biblioteca.cadastrar_livro(titulo="Python Fluente",
                           editora="O'Reilly",
                           numero=1,
                           edicao=2,
                           autores=[autor],
                           genero="Programação"
                           )

biblioteca.cadastrar_livro(titulo="Python Fluente",
                           editora="O'Reilly",
                           numero=2,
                           edicao=2,
                           autores=[autor],
                           genero="Programação"
                           )

print("Livros que a biblioteca possui: ")
biblioteca.listar_livros()

usuario_1 = biblioteca.cadastrar_usuario(nome="João Silva", nacionalidade="Brasileiro", telefone="987654321")
usuario_2 = biblioteca.cadastrar_usuario(nome="Maria Silva", nacionalidade="Brasileira", telefone="987653123")

print("\n\nUsuarios cadastrados na biblioteca: ")
biblioteca.listar_usuarios()

emprestimo_1 = biblioteca.registrar_emprestimo(usuario_1, "Python Fluente")
emprestimo_2 = biblioteca.registrar_emprestimo(usuario_2, "Python Fluente")
print("\n\nHistórico de empréstimos da biblioteca: ")
biblioteca.listar_emprestimos()

print("\n\nLivros que atualizados após empréstimos: ")
biblioteca.listar_livros()


biblioteca.devolver_exemplar(emprestimo_1)
print("\n\nLivros que atualizados após devolução: ")
biblioteca.listar_livros()
print("\n\nHistórico de empréstimos da biblioteca: ")
biblioteca.listar_emprestimos()


