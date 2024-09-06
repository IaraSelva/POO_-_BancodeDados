import sqlite3
from sqlite3 import IntegrityError

# Classe Abstrata
class Pessoa:
    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade

# Herança
class Autor(Pessoa):
    pass

# Herança
class Usuario:
    def __init__(self, nome, telefone, nacionalidade, id=None):
        self.nome = nome
        self.telefone = telefone
        self.nacionalidade = nacionalidade
        self.id = id
        
    def save_to_db(self):
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()

        try:
            if self.id is None:
                cursor.execute('''
                INSERT INTO Usuarios (nome, telefone, nacionalidade)
                VALUES (?, ?, ?)
                ''', (self.nome, self.telefone, self.nacionalidade))
                self.id = cursor.lastrowid
            else:
                cursor.execute('''
                UPDATE Usuarios
                SET nome = ?, telefone = ?, nacionalidade = ?
                WHERE id = ?
                ''', (self.nome, self.telefone, self.nacionalidade, self.id))
                
            conn.commit()
        except IntegrityError:
            print("Erro: Já existe um usuário cadastrado com mesmo nome e telefone.")
        finally:
            conn.close()


class Biblioteca:
    def __init__(self):
        self.conn = sqlite3.connect('biblioteca.db')
        self.cursor = self.conn.cursor()

    def cadastrar_usuario(self, nome, nacionalidade, telefone):
        novo_usuario = Usuario(nome=nome, nacionalidade=nacionalidade, telefone=telefone)
        novo_usuario.save_to_db()
        return novo_usuario

    def listar_usuarios(self):
        self.cursor.execute('SELECT * FROM Usuarios')
        usuarios = self.cursor.fetchall()
        for usuario in usuarios:
            print(usuario)

    def close(self):
        self.conn.close()


# Exemplo de uso
biblioteca = Biblioteca()

biblioteca.cadastrar_usuario(nome="Maciel Silva", nacionalidade="Brasileiro", telefone="987654322")
biblioteca.cadastrar_usuario(nome="Antonia Silva", nacionalidade="Brasileira", telefone="987653124")

print("\n\nUsuarios cadastrados na biblioteca: ")
biblioteca.listar_usuarios()

biblioteca.close()

