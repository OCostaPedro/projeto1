from utils import limpar_tela, pausar


def calcular_nivel(minutos):
    if minutos <= 900:
        return "SILVER 🥈", "basico"
    elif minutos <= 1800:
        return "GOLD 🥇", "basico"
    else:
        return "DIAMOND 💎", "avancado"


def mostrar_nivel(usuario):
    limpar_tela()
    print("●" * 50)
    print("SEU NÍVEL DE USUÁRIO")
    print("●" * 50)
    
    nivel, tipo = calcular_nivel(usuario["minutos"])
    
    print(f"\nUsuário: {usuario['nome']}")
    print(f"Seu nível é: {nivel}")
    print(f"Sua quantidade de minutos: {usuario['minutos']}")
    
    print("\n Tabela de Níveis:")
    print("   🥈 SILVER: 0 a 900 min (0 a 15h)")
    print("   🥇 GOLD: 901 a 1.800 min (16 a 30h)")
    print("   💎 DIAMOND: acima de 1.801 min (mais de 30h)")
    
    print("●" * 50)
    pausar()
    return tipo