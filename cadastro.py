import os
os.system("cls")

pessoas = {}
proximo_id = 1

while True:
    print("\nMenu de Opções:")
    print("1. Inserir nome")
    print("2. Mostrar nomes")
    print("3. Atualizar nome")
    print("4. Deletar nome")
    print("5. Sair")
    
    opcao = int(input("Digite a opção desejada: "))
    
    if opcao == 1:
        nome = input("Digite o nome que deseja inserir: ")
        pessoas[proximo_id] = nome
        print(f"Nome adicionado com ID: {proximo_id}")
        proximo_id += 1
    
    elif opcao == 2:
        if pessoas:
            print("Mostrar de nomes:")
            for id, nome in pessoas.items():
                print(f"ID {id}: {nome}")
        else:
            print("Nenhum nome cadastrado.")
    
    elif opcao == 3:
        id_pessoa = int(input("Digite o ID do nome que deseja atualizar: "))
        if id_pessoa in pessoas:
            novo_nome = input("Digite o novo nome: ")
            pessoas[id_pessoa] = novo_nome
            print("Nome atualizado com sucesso!")
        else:
            print("ID inválido.")
    
    elif opcao == 4:
        id_pessoa = int(input("Digite o ID do nome que deseja deletar: "))
        if id_pessoa in pessoas:
            del pessoas[id_pessoa]
            print("Nome deletado com sucesso!")
        else:
            print("ID inválido.")
    
    elif opcao == 5:
        print("Fim.")
        break
    
    else:
        print("Opção inválida.")