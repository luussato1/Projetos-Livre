import tkinter as tk
from tkinter import messagebox, simpledialog
from .livro import Livro
from .pessoa import Usuario, Funcionario
from .dados import salvar_dados, carregar_dados
from .biblioteca import Biblioteca

class BibliotecaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Biblioteca")

        self.biblioteca = carregar_dados("biblioteca.pkl")
        if not self.biblioteca:
            messagebox.showinfo("Info", "Nenhum dado encontrado. Criando nova biblioteca.")
            self.biblioteca = Biblioteca("Biblioteca Central")
            self._criar_usuarios_padrao()
            self._criar_funcionarios_padrao()

        self.frame = tk.Frame(root)
        self.frame.pack(padx=20, pady=20)

        # Botões do sistema
        botoes = [
            ("Cadastrar Livro", self.cadastrar_livro),
            ("Exibir Livros Disponíveis", self.listar_livros),
            ("Listar Usuários", self.listar_usuarios),
            ("Cadastrar Usuário", self.cadastrar_usuario),  # <-- AQUI ESTÁ O BOTÃO QUE FALTAVA
            ("Cadastrar Funcionário", self.cadastrar_funcionario),
            ("Listar Funcionários", self.listar_funcionarios),
            ("Emprestar Livro", self.emprestar_livro),
            ("Devolver Livro", self.devolver_livro),
            ("Sair e Salvar", self.sair)
        ]

        for texto, comando in botoes:
            tk.Button(self.frame, text=texto, command=comando).pack(pady=2)

    def _criar_usuarios_padrao(self):
        self.biblioteca.adicionar_usuario(Usuario("Alice", 1))
        self.biblioteca.adicionar_usuario(Usuario("Bruno", 2))

    def _criar_funcionarios_padrao(self):
        self.biblioteca.adicionar_funcionario(Funcionario("Carlos", 1))

    def cadastrar_livro(self):
        titulo = simpledialog.askstring("Título", "Digite o título do livro:")
        autor = simpledialog.askstring("Autor", "Digite o nome do autor:")
        codigo = simpledialog.askstring("Código", "Digite o código do livro:")

        if titulo and autor and codigo:
            livro = Livro(titulo, autor, codigo)
            self.biblioteca.cadastrar_livro(livro)
            messagebox.showinfo("Sucesso", f"Livro '{titulo}' cadastrado com sucesso!")
        else:
            messagebox.showwarning("Erro", "Todos os campos devem ser preenchidos.")

    def cadastrar_usuario(self):
        nome = simpledialog.askstring("Nome", "Digite o nome do usuário:")
        id_usuario = simpledialog.askinteger("ID", "Digite o ID do usuário:")

        if nome and id_usuario is not None:
            usuario = Usuario(nome, id_usuario)
            self.biblioteca.adicionar_usuario(usuario)
            messagebox.showinfo("Sucesso", f"Usuário '{nome}' cadastrado com sucesso!")
        else:
            messagebox.showwarning("Erro", "Todos os campos devem ser preenchidos.")

    def listar_livros(self):
        livros = self.biblioteca.livros_disponiveis()
        if livros:
            texto = "\n".join([f"{livro.titulo} ({livro.codigo})" for livro in livros])
        else:
            texto = "Nenhum livro disponível no momento."
        messagebox.showinfo("Livros Disponíveis", texto)

    def listar_usuarios(self):
        if not self.biblioteca.usuarios:
            messagebox.showinfo("Usuários", "Nenhum usuário cadastrado.")
            return

        texto = "\n".join([f"Nome: {u.nome} | ID: {u.id_usuario}" for u in self.biblioteca.usuarios])
        messagebox.showinfo("Usuários", texto)

    def cadastrar_funcionario(self):
        nome = simpledialog.askstring("Nome", "Digite o nome do funcionário:")
        id_funcionario = simpledialog.askinteger("ID", "Digite o ID do funcionário:")

        if nome and id_funcionario is not None:
            funcionario = Funcionario(nome, id_funcionario)
            self.biblioteca.adicionar_funcionario(funcionario)
            messagebox.showinfo("Sucesso", f"Funcionário '{nome}' cadastrado com sucesso!")
        else:
            messagebox.showwarning("Erro", "Todos os campos devem ser preenchidos.")

    def listar_funcionarios(self):
        if not self.biblioteca.funcionarios:
            messagebox.showinfo("Funcionários", "Nenhum funcionário cadastrado.")
            return

        texto = "\n".join([f"Nome: {f.nome} | ID: {f.id_funcionario}" for f in self.biblioteca.funcionarios])
        messagebox.showinfo("Funcionários", texto)

    def emprestar_livro(self):
        if not self.biblioteca.funcionarios:
            messagebox.showwarning("Erro", "Nenhum funcionário cadastrado para processar o empréstimo.")
            return

        funcionario = self.biblioteca.funcionarios[0]
        id_usuario = simpledialog.askinteger("ID do Usuário", "Digite o ID do usuário:")
        codigo_livro = simpledialog.askstring("Código do Livro", "Digite o código do livro:")

        if id_usuario is not None and codigo_livro:
            sucesso, mensagem = self.biblioteca.emprestar_livro(codigo_livro, id_usuario, funcionario)
            if sucesso:
                messagebox.showinfo("Sucesso", mensagem)
            else:
                messagebox.showwarning("Erro", mensagem)

    def devolver_livro(self):
        id_usuario = simpledialog.askinteger("ID do Usuário", "Digite o ID do usuário:")
        codigo_livro = simpledialog.askstring("Código do Livro", "Digite o código do livro:")

        if id_usuario is not None and codigo_livro:
            sucesso, mensagem = self.biblioteca.devolver_livro(codigo_livro, id_usuario)
            if sucesso:
                messagebox.showinfo("Sucesso", mensagem)
            else:
                messagebox.showwarning("Erro", mensagem)

    def sair(self):
        salvar_dados("biblioteca.pkl", self.biblioteca)
        self.root.quit()
