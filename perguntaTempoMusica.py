def make_music_green():
    print("🎵🌱 Bem-vindo ao aplicativo MAKE MUSIC GREEN! 🌱🎵")
    print("\nQueremos saber: quanto tempo você ouve música por dia?\n")
    
    print("1 - Menos de 1 hora")
    print("2 - Entre 1 e 3 horas")
    print("3 - Entre 3 e 5 horas")
    print("4 - Mais de 5 horas\n")

    escolha = input("Digite o número da opção que mais combina com você: ")

    if escolha == "1":
        print("\nExcelente! Seu consumo de música é leve e sustentável. 💚")
    elif escolha == "2":
        print("\nBom equilíbrio! Tente baixar suas músicas favoritas para reduzir o streaming. 🌿")
    elif escolha == "3":
        print("\nAtenção! Esse tempo já representa um consumo energético considerável. ⚠️")
    elif escolha == "4":
        print("\nOps! Ouvir tanta música por streaming pode aumentar seu impacto ambiental. 🌍\nTente equilibrar e apoiar práticas mais verdes!")
    else:
        print("\nOps! Opção inválida. Tente novamente digitando um número de 1 a 4. 😅")

# Executa o aplicativo
make_music_green()