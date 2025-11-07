import os

def menu():
    print("\nMenu de Opções:")
    print("1. Inserir nome")
    print("2. Mostrar nomes")
    print("3. Atualizar nome")
    print("4. Deletar nome")
    print("5. Sair")
    return int(input("Digite a opção desejada: "))

def inserir(pessoas, proximo_id):
    nome = input("Digite o nome que deseja inserir: ")
    pessoas[proximo_id] = nome
    print(f"Nome adicionado com ID: {proximo_id}")
    return proximo_id + 1

def mostrar(pessoas):
    if pessoas:
        print("Mostrar de nomes:")
        for id_, nome in pessoas.items():
            print(f"ID {id_}: {nome}")
    else:
        print("Nenhum nome cadastrado.")

def atualizar(pessoas):
    id_pessoa = int(input("Digite o ID do nome que deseja atualizar: "))
    if id_pessoa in pessoas:
        novo_nome = input("Digite o novo nome: ")
        pessoas[id_pessoa] = novo_nome
        print("Nome atualizado com sucesso!")
    else:
        print("ID inválido.")

def deletar(pessoas):
    id_pessoa = int(input("Digite o ID do nome que deseja deletar: "))
    if id_pessoa in pessoas:
        del pessoas[id_pessoa]
        print("Nome deletado com sucesso!")
    else:
        print("ID inválido.")

def main():
    os.system("cls" if os.name == "nt" else "clear")
    pessoas = {}
    proximo_id = 1

    while True:
        opcao = menu()

        if opcao == 1:
            proximo_id = inserir(pessoas, proximo_id)
        elif opcao == 2:
            mostrar(pessoas)
        elif opcao == 3:
            atualizar(pessoas)
        elif opcao == 4:
            deletar(pessoas)
        elif opcao == 5:
            print("Fim.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
