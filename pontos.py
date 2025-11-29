from utils import limpar_tela, pausar
from nivel import calcular_nivel


def calcular_pontos_por_nivel(minutos):
    if minutos <= 900:
        return 5  # SILVER
    elif minutos <= 1800:
        return 10  # GOLD
    else:
        return 15  # DIAMOND


def mostrar_pontos(usuario):
    limpar_tela()
    print("●" * 50)
    print("PONTOS E RECOMPENSAS")
    print("●" * 50)
    
    nivel_nome = calcular_nivel(usuario['minutos'])[0]
    pontos_por_jogada = calcular_pontos_por_nivel(usuario['minutos'])
    
    print(f"\nUsuário: {usuario['nome']}")
    print(f"Nível atual: {nivel_nome}")
    print(f"Pontos acumulados: {usuario['pontos_acumulados']} pontos")
    print(f"Pontos por jogada: {pontos_por_jogada} pontos")
    
    print("\n" + "●" * 50)
    print("META DE RECOMPENSA")
    print("●" * 50)
    
    pontos_faltando = 1000 - usuario['pontos_acumulados']
    
    if usuario['pontos_acumulados'] >= 1000:
        print("\nPARABÉNS! Você atingiu a meta de 1.000 pontos!")
        print("Você pode resgatar seu desconto de 10% na")
        print("   assinatura do Spotify Premium mensal!")
        excedente = usuario['pontos_acumulados'] - 1000
        if excedente > 0:
            print(f"\n💎 Você tem {excedente} pontos extras!")
    else:
        print(f"\n🎯 Faltam {pontos_faltando} pontos para alcançar 1.000 pontos")
        print("🎵 Meta: Ganhar desconto de 10% no Spotify Premium")
        
        # Calcula quantas jogadas faltam
        jogadas_necessarias = (pontos_faltando + pontos_por_jogada - 1) // pontos_por_jogada
        print(f"\nCom seu nível atual ({nivel_nome}), você precisa de")
        print(f"   aproximadamente {jogadas_necessarias} jogadas para atingir a meta!")
    
    print("\n" + "=" * 50)
    print("TABELA DE PONTOS POR NÍVEL")
    print("●" * 50)
    print("\n   🥈 SILVER: 5 pontos por jogada")
    print("   🥇 GOLD: 10 pontos por jogada")
    print("   💎 DIAMOND: 15 pontos por jogada")
    
    print("\n🌍 Cada jogada ajuda o meio ambiente através da compra")
    print("   de créditos de carbono!")
    
    print("●" * 50)
    pausar()