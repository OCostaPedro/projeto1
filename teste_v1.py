import os
os.system ("cls")
def introducao():
 print("Bem Vindo ao Make Music Green!\n" \
 \
 "Make Music Green é um WebApp inovador que transforma o modo como você se relaciona com a música e o meio ambiente. " \
 "De forma lúdica e interativa, ele ajuda você a reduzir sua pegada ecológica digital, mostrando o impacto ambiental do seu streaming musical." \
 "Ao contrário das simples calculadoras de CO₂, o Make Music Green vai além! Ele exibe indicadores reais de poluição gerada pelo uso das plataformas de streaming e sugere ações personalizadas para compensar esse impacto fazendo isso tudo dentro de uma experiência gamificada e divertida.\n" \
 "Crie uma conta e nos ajude a fazer o mundo um lugar melhor!")
 print(introducao())

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
import os
os.system("cls")

media_emissao_CO2_pessoa = 27
media_minutos_por_pessoa_brasil = 1243  
ano = 12 

minutos_musica = int(input("Insira quantos minutos de música você escutou no último mês: "))

consumo_co2 = (media_emissao_CO2_pessoa*minutos_musica)/media_minutos_por_pessoa_brasil

if consumo_co2 <= 900:
    print(f"Nesse ritmo, em um ano você emitirá {consumo_co2*ano} gramas de CO².")
    print(f"\nSe todos os usuários do Spotify Brasil seguissem o seu ritmo, seriam emitidas {consumo_co2*12*56000000} toneladas de CO² em um ano.")
    print("Isso seria um valor menor do que o total atual.")

elif consumo_co2 > 900 and consumo_co2 <= 1800:
    print(f"Nesse ritmo, em um ano você emitirá {consumo_co2*ano} gramas de CO².")
    print(f"\nSe todos os usuários do Spotify Brasil seguissem o seu ritmo, seriam emitidas {consumo_co2*12*56000000} toneladas de CO² em um ano.")
    print("Isso seria um valor equivalente ao total atual.")

elif consumo_co2 > 1801:
    print(f"Nesse ritmo, em um ano você emitirá {consumo_co2*ano} gramas de CO².")
    print(f"\nSe todos os usuários do Spotify Brasil seguissem o seu ritmo, seriam emitidas {consumo_co2*12*56000000} toneladas de CO² em um ano.")
    print("Isso seria um valor maior do que o total atual.")    

def exibir_emissao_spotify(clear=True):
    if clear:
        os.system('cls' if os.name == 'nt' else 'clear')
    print("A emissão anual pelo consumo de música pelo streaming Spotify é de 195 mil e 27 toneladas métricas de gás carbônico.\n")
    print("Isso equivale a:\n")
    print("A emissão de CO2 de 45 mil carros durante 1 ano\n")
    print("A emissão de CO2 de 55.260 casas durante 1 ano\n")
    print("A emissão de CO2 de 181 mil voos de São Paulo-Rio a Janeiro\n")
    print("Fonte: EPA https://www.epa.gov/energy/greenhouse-gas-equivalencies-calculator")

if __name__ == "__main__":
    exibir_emissao_spotify()

def consumo_baixo():
    print("Seu tempo de consumo é BAIXO \n"
    "Com um tempo entre 0-30h(0 a 901 min), sua pegada ecológica,"
    "é de pequena proporção comparada as demais, mas ainda sim é importante agir para evitar o acúmulo.") 
print(consumo_baixo())

def consumo_medio():
    print("Seu tempo de consumo é MÉDIO \n"  \
    "Com um tempo entre 16-30h(901 a 1800 min), sua pegada ecológica," \
    "não é das maiores proporções, mas ainda assim é necessário que algo seja feito para não acumular.") 
print(consumo_medio())

def consumo_alto():
      print("Seu tempo de consumo é ALTO \n"
      "Com um tempo acima de 30h (mais de 1800 min), sua pegada ecológica"
      "é elevada e exige mudanças imediatas para reduzir os impactos e evitar acúmulos.")
print(consumo_alto())
