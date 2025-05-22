class Pessoa:
    def __init__(self, nome):
        self.nome = nome


class Usuario(Pessoa):
    def __init__(self, nome, id_usuario):
        super().__init__(nome)
        self.id_usuario = id_usuario
        self.historico = []

    def registrar_historico(self, mensagem):
        self.historico.append(mensagem)


class Funcionario(Pessoa):
    def __init__(self, nome, id_funcionario):
        super().__init__(nome)
        self.id_funcionario = id_funcionario
