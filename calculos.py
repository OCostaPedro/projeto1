import os
os.system("cls")

minutos_musica = int(input("Insira quantos minutos de música você escutou no último mês: "))

consumo_co2 = (27*minutos_musica)/1243

if consumo_co2 <= 900:
    print(f"Nesse ritmo, em um ano você emitirá {consumo_co2*12} gramas de CO².")
    print(f"\nSe todos os usuários do Spotify Brasil seguissem o seu ritmo, seriam emitidas {consumo_co2*12*56000000} toneladas de CO² em um ano.")
    print("Isso seria um valor menor do que o total atual.")

elif consumo_co2 > 900 and consumo_co2 <= 1800:
    print(f"Nesse ritmo, em um ano você emitirá {consumo_co2*12} gramas de CO².")
    print(f"\nSe todos os usuários do Spotify Brasil seguissem o seu ritmo, seriam emitidas {consumo_co2*12*56000000} toneladas de CO² em um ano.")
    print("Isso seria um valor equivalente ao total atual.")

elif consumo_co2 > 1800:
    print(f"Nesse ritmo, em um ano você emitirá {consumo_co2*12} gramas de CO².")
    print(f"\nSe todos os usuários do Spotify Brasil seguissem o seu ritmo, seriam emitidas {consumo_co2*12*56000000} toneladas de CO² em um ano.")
    print("Isso seria um valor maior do que o total atual.")    
