def adicionar_contato(contatos):
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    contatos.append({'nome': nome, 'telefone': telefone})
    print("Contato adicionado com sucesso!")

def remover_contato(contatos):
    nome = input("Digite o nome do contato a ser removido: ")
    for contato in contatos:
        if contato['nome'] == nome:
            contatos.remove(contato)
            print(f"Contato {nome} removido com sucesso!")
            return
    print("Contato não encontrado!")

def editar_contato(contatos):
    nome = input("Digite o nome do contato a ser editado: ")
    for contato in contatos:
        if contato['nome'] == nome:
            novo_nome = input(f"Digite o novo nome para {nome}: ")
            novo_telefone = input(f"Digite o novo telefone para {nome}: ")
            contato['nome'] = novo_nome
            contato['telefone'] = novo_telefone
            print(f"Contato {nome} editado com sucesso!")
            return
    print("Contato não encontrado!")

def visualizar_contatos(contatos):
    if not contatos:
        print("Não há contatos na agenda.")
    else:
        for contato in contatos:
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}")

def menu_estruturado():
    contatos = []
    while True:
        print("\nAgenda de Contatos:")
        print("1. Adicionar Contato")
        print("2. Remover Contato")
        print("3. Editar Contato")
        print("4. Visualizar Contatos")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            adicionar_contato(contatos)
        elif opcao == '2':
            remover_contato(contatos)
        elif opcao == '3':
            editar_contato(contatos)
        elif opcao == '4':
            visualizar_contatos(contatos)
        elif opcao == '5':
            print("Saindo da agenda.")
            break
        else:
            print("Opção inválida. Tente novamente.")

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, nome, telefone):
        self.contatos.append({'nome': nome, 'telefone': telefone})
        print("Contato adicionado com sucesso!")

    def remover_contato(self, nome):
        for contato in self.contatos:
            if contato['nome'] == nome:
                self.contatos.remove(contato)
                print(f"Contato {nome} removido com sucesso!")
                return
        print("Contato não encontrado!")

    def editar_contato(self, nome, novo_nome, novo_telefone):
        for contato in self.contatos:
            if contato['nome'] == nome:
                contato['nome'] = novo_nome
                contato['telefone'] = novo_telefone
                print(f"Contato {nome} editado com sucesso!")
                return
        print("Contato não encontrado!")

    def visualizar_contatos(self):
        if not self.contatos:
            print("Não há contatos na agenda.")
        else:
            for contato in self.contatos:
                print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}")

def menu_orientado_a_objetos():
    agenda = Agenda()
    while True:
        print("\nAgenda de Contatos:")
        print("1. Adicionar Contato")
        print("2. Remover Contato")
        print("3. Editar Contato")
        print("4. Visualizar Contatos")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            agenda.adicionar_contato(nome, telefone)
        elif opcao == '2':
            nome = input("Digite o nome do contato a ser removido: ")
            agenda.remover_contato(nome)
        elif opcao == '3':
            nome = input("Digite o nome do contato a ser editado: ")
            novo_nome = input(f"Digite o novo nome para {nome}: ")
            novo_telefone = input(f"Digite o novo telefone para {nome}: ")
            agenda.editar_contato(nome, novo_nome, novo_telefone)
        elif opcao == '4':
            agenda.visualizar_contatos()
        elif opcao == '5':
            print("Saindo da agenda.")
            break
        else:
            print("Opção inválida. Tente novamente.")

def main():
    print("Escolha o paradigma de programação:")
    print("1. Paradigma Estruturado")
    print("2. Paradigma Orientado a Objetos")
    
    escolha = input("Escolha a opção (1 ou 2): ")
    
    if escolha == '1':
        menu_estruturado()
    elif escolha == '2':
        menu_orientado_a_objetos()
    else:
        print("Opção inválida. Saindo.")
        
main()