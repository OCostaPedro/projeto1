import random
import time
from utils import limpar_tela, pausar
from nivel import calcular_nivel
from cadastro import carregar_usuarios, atualizar_usuarios
from datetime import datetime


def selecionar_genero():
    limpar_tela()
    print("●" * 60)
    print("  ESCOLHA SEU GÊNERO MUSICAL FAVORITO")
    print("●" * 60)
    print("\n1 - ROCK")
    print("2 - POP")
    print("3 - MPB")
    print("4 - SERTANEJO")
    print("5 - FUNK")
    print("6 - HIP HOP")
    print("7 - FORRÓ")
    print("8 - PAGODE/SAMBA")
    print("●" * 60)
    
    while True:
        opcao = input("\nEscolha uma opção (1-8): ").strip()
        
        if opcao == "1":
            return "rock", "questoes_rock.txt"
        elif opcao == "2":
            return "pop", "questoes_pop.txt"
        elif opcao == "3":
            return "mpb", "questoes_mpb.txt"
        elif opcao == "4":
            return "sertanejo", "questoes_sertanejo.txt"
        
        else:
            print("Opção inválida! Digite um número de 1 a 4.")


def carregar_questoes(arquivo):
    questoes = []
    
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            linhas = f.readlines()
            
            i = 0
            while i < len(linhas):
                linha = linhas[i].strip()
                
                # Ignora linhas vazias
                if not linha:
                    i += 1
                    continue
                
                # Linha com a pergunta
                pergunta = linha
                opcoes = []
                resposta = ""
                
                # Lê as 4 opções
                i += 1
                for _ in range(4):
                    if i < len(linhas):
                        opcao = linhas[i].strip()
                        if opcao:
                            opcoes.append(opcao)
                        i += 1
                
                # Lê a resposta (próxima linha após as opções)
                if i < len(linhas):
                    resp_linha = linhas[i].strip()
                    if resp_linha.startswith("Resposta:") or resp_linha.startswith("Gabarito:"):
                        resposta = resp_linha.split(":")[-1].strip().lower()
                        i += 1  # avança além da linha da resposta

                # Se encontrou pergunta com 4 opções e resposta, adiciona
                if len(opcoes) == 4 and resposta:
                    questoes.append({
                        "pergunta": pergunta,
                        "opcoes": opcoes,
                        "resposta": resposta
                    })
                # não faz i += 1 aqui; já avançamos ao longo da leitura

    except FileNotFoundError:
        print(f"\nArquivo {arquivo} não encontrado!")
    
    return questoes


def carregar_quiz(usuario):
    limpar_tela()
    print("\n⏳ Carregando quiz", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print(" ✅")
    time.sleep(1)
    
    # Anúncio
    limpar_tela()
    print("Por favor não pule esse anúncio! Assista 5s de anúncio para ganhar pontos extras.")
    print("\n-------ANÚNCIO------")
    print("Venha conhecer a FORJA na Mostra Tech Design do CESAR!")
    print("\nAlém dos clássicos que você já conhece,")
    print("lançaremos o mais novo jogo: FrevoPlay.")
    print("Um 'genius' massa que valoriza a cultura pernambucana.")
    print("É diversão garantida! Não perca!")
    print("--------------------")
    print("\nAguarde 5 segundos...", end="", flush=True)
    for _ in range(5):
        time.sleep(1)
        print(".", end="", flush=True)
    print(" Pronto!")
    time.sleep(0.5)
    
    # Adiciona 5 pontos por assistir o anúncio
    usuario["pontos_acumulados"] += 5
    print("\n+5 pontos por assistir o anúncio!")
    time.sleep(1.5)
    
    return 5  # Retorna os pontos ganhos pelo anúncio


def sortear_perguntas(arquivo_questoes):
    questoes = carregar_questoes(arquivo_questoes)
    
    if len(questoes) < 10:
        print(f"\nAtenção: Apenas {len(questoes)} questões disponíveis!")
        return questoes
    
    random.shuffle(questoes)
    return questoes[:10]


def calcular_pontos_por_nivel(minutos):
    """Calcula quantos pontos o usuário ganha baseado no nível (tempo em minutos)."""
    if minutos <= 900:
        return 15  # SILVER
    elif minutos <= 1800:
        return 10  # GOLD
    else:
        return 5   # DIAMOND


def salvar_respostas(usuario, perguntas, respostas_usuario, acertos, pontos_ganhos, genero):
    with open("respostas.txt", "a", encoding="utf-8") as arquivo:
        total_perguntas = len(perguntas)
        arquivo.write("=" * 60 + "\n")
        arquivo.write(f"USUÁRIO: {usuario['nome']} ({usuario['email']})\n")
        arquivo.write(f"DATA: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        arquivo.write(f"GÊNERO: {genero.upper()}\n")
        arquivo.write(f"NÍVEL: {calcular_nivel(usuario['minutos'])[0]}\n")
        arquivo.write(f"PONTUAÇÃO: {acertos}/{total_perguntas} ({(acertos / total_perguntas) * 100:.1f}%)\n")
        arquivo.write(f"PONTOS GANHOS: +{pontos_ganhos} pontos\n")
        arquivo.write(f"TOTAL DE PONTOS: {usuario['pontos_acumulados']} pontos\n")
        arquivo.write("=" * 60 + "\n\n")
        
        for i, (pergunta, resposta) in enumerate(zip(perguntas, respostas_usuario), 1):
            correto = "✅" if resposta == pergunta["resposta"] else "❌"
            arquivo.write(f"PERGUNTA {i}: {pergunta['pergunta']}\n")
            arquivo.write(f"Resposta do usuário: {resposta.upper()} {correto}\n")
            arquivo.write(f"Resposta correta: {pergunta['resposta'].upper()}\n\n")
        
        arquivo.write("\n")


def mostrar_resultado(usuario, acertos, pontos_ganhos):
    limpar_tela()
    print("●" * 50)
    print("  RESULTADO DO QUIZ")
    print("●" * 50)
    
    print(f"\n{usuario['nome']}")
    print(f"Acertos: {acertos}/10")  # assumindo 10 questões no quiz

    nivel_nome = calcular_nivel(usuario['minutos'])[0]
    print(f"\nVocê conquistou {pontos_ganhos} pontos! (Nível {nivel_nome})")
    print(f"Total de pontos acumulados: {usuario['pontos_acumulados']} pontos")
    
    pontos_faltando = 1000 - usuario['pontos_acumulados']
    
    if usuario['pontos_acumulados'] >= 1000:
        print("\nPARABÉNS! Você já tem pontos suficientes!")
        print("Você pode receber um desconto de 10%")
        print("na assinatura do Spotify Premium!")
    else:
        print(f"\nFaltam {pontos_faltando} pontos para ganhar seu desconto!")
        print("Junte 1.000 pontos para receber um desconto de 10%")
        print("na assinatura do Spotify Premium!")
    
    print("\n" + "●" * 50)
    
    print("\nCada ação que você faz importa!")
    print("Com a sua jogada, nós podemos comprar créditos de carbono")
    print("para compensar a sua emissão de gás carbônico!")
    print("●" * 50)
    
    pausar()


def aplicar_quiz(usuario):
    # Seleciona o gênero
    genero_nome, arquivo_questoes = selecionar_genero()
    
    nivel, tipo_nivel = calcular_nivel(usuario["minutos"])
    pontos_anuncio = carregar_quiz(usuario)
    
    perguntas = sortear_perguntas(arquivo_questoes)
    
    if len(perguntas) == 0:
        print("\nNão há questões disponíveis para este gênero!")
        pausar()
        return
    
    acertos = 0
    respostas_usuario = []
    
    limpar_tela()
    print("●" * 50)
    print(f"  QUIZ {genero_nome.upper()} - NÍVEL {nivel}")
    print("●" * 50)
    print(f"\nResponda as {len(perguntas)} perguntas abaixo:\n")
    pausar()
    
    for i, questao in enumerate(perguntas, 1):
        limpar_tela()
        print(f"PERGUNTA {i}/{len(perguntas)}")
        print("●" * 50)
        print(f"\n{questao['pergunta']}\n")
        
        for opcao in questao['opcoes']:
            print(opcao)
        
        resposta = input("\nSua resposta (a/b/c/d): ").strip().lower()
        while resposta not in ("a", "b", "c", "d"):
            print("Resposta inválida! Digite apenas a, b, c ou d.")
            resposta = input("Sua resposta (a/b/c/d): ").strip().lower()

        respostas_usuario.append(resposta)
        
        if resposta == questao['resposta']:
            print("Correto!")
            acertos += 1
        else:
            print(f"Errado! A resposta correta era: {questao['resposta']}")
        
        time.sleep(1.5)
    
    pontos_quiz = calcular_pontos_por_nivel(usuario["minutos"])
    total_pontos_ganhos = pontos_quiz + pontos_anuncio
    
    usuario["pontuacao"] = acertos
    # Adiciona só os pontos do quiz (os do anúncio já foram somados em carregar_quiz)
    usuario["pontos_acumulados"] += pontos_quiz  
    
    usuarios = carregar_usuarios()
    for u in usuarios:
        if u["email"] == usuario["email"]:
            u["pontuacao"] = acertos
            u["pontos_acumulados"] = usuario["pontos_acumulados"]
            break
    atualizar_usuarios(usuarios)
    
    salvar_respostas(usuario, perguntas, respostas_usuario, acertos, total_pontos_ganhos, genero_nome)
    
    mostrar_resultado(usuario, acertos, total_pontos_ganhos)
