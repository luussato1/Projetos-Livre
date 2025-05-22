
# biblioteca.py
from .historico import HistoricoMixin
from .emprestimo import Emprestimo

class Biblioteca(HistoricoMixin):
    def __init__(self, nome):
        self.nome = nome
        self.livros = []
        self.usuarios = []
        self.funcionarios = []
        self.emprestimos = []

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)
        self.registrar(f"Usuário {usuario.nome} adicionado.")

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
        self.registrar(f"Funcionário {funcionario.nome} adicionado.")

    def cadastrar_livro(self, livro):
        self.livros.append(livro)
        self.registrar(f"Livro '{livro.titulo}' cadastrado.")

    def emprestar_livro(self, codigo_livro, id_usuario, funcionario):
        livro = next((l for l in self.livros if l.codigo == codigo_livro and l.disponivel), None)
        usuario = next((u for u in self.usuarios if u.id == id_usuario), None)
        if livro and usuario:
            livro.disponivel = False
            emprestimo = Emprestimo(livro, usuario)
            self.emprestimos.append(emprestimo)
            usuario.registrar_historico(f"Emprestado: {livro.titulo}")
            self.registrar(f"Livro '{livro.titulo}' emprestado para {usuario.nome} por {funcionario.nome}.")

    def devolver_livro(self, codigo_livro, id_usuario):
        emprestimo = next((e for e in self.emprestimos if e.livro.codigo == codigo_livro and e.usuario.id == id_usuario), None)
        if emprestimo:
            emprestimo.livro.disponivel = True
            emprestimo.usuario.registrar_historico(f"Devolvido: {emprestimo.livro.titulo}")
            self.registrar(f"Livro '{emprestimo.livro.titulo}' devolvido por {emprestimo.usuario.nome}.")
            self.emprestimos.remove(emprestimo)

    def livros_disponiveis(self):
        return [l for l in self.livros if l.disponivel]
