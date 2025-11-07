import os

def calcular_consumo_co2(minutos_musica):
    return (27 * minutos_musica) / 1243

def exibir_resultados(minutos_musica):
    consumo_co2 = calcular_consumo_co2(minutos_musica)
    print(f"Nesse ritmo, em um ano você emitirá {consumo_co2 * 12} gramas de CO².")
    print(f"\nSe todos os usuários do Spotify Brasil seguissem o seu ritmo, seriam emitidas {consumo_co2 * 12 * 56000000} toneladas de CO² em um ano.")
    if consumo_co2 <= 900:
        print("Isso seria um valor menor do que o total atual.")
    elif consumo_co2 <= 1800:
        print("Isso seria um valor equivalente ao total atual.")
    else:
        print("Isso seria um valor maior do que o total atual.")

def main():
    os.system("cls" if os.name == "nt" else "clear")
    minutos_musica = int(input("Insira quantos minutos de música você escutou no último mês: "))
    exibir_resultados(minutos_musica)

if __name__ == "__main__":
    main()
