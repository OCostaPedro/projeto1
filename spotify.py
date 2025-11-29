
from utils import limpar_tela, pausar
from cadastro import carregar_usuarios, atualizar_usuarios


def mostrar_instrucoes_spotify():
    limpar_tela()
    print("●" * 50)
    print("  COMO OBTER SEU TEMPO DE MÚSICA NO SPOTIFY")
    print("●" * 50)
    print("\n1️.  Abra o aplicativo do Spotify")
    print("2️.  Vá até seu perfil")
    print("3️.  Procure pela opção 'Cápsula Sonora'")
    print("4️.  Lá você verá os minutos ouvidos no mês!")
    print("\n Insira os minutos na próxima etapa.")
    print("●" * 50)
    pausar()


def inserir_minutos(usuario):
    limpar_tela()
    print("●" * 50)
    print("  INSIRA SEU TEMPO DE MÚSICA")
    print("●" * 50)
    
    try:
        minutos = int(input("\nQuantos MINUTOS você ouviu de música este mês? "))
        usuario["minutos"] = minutos
        
        # Atualiza o arquivo de usuários
        usuarios = carregar_usuarios()
        for u in usuarios:
            if u["email"] == usuario["email"]:
                u["minutos"] = minutos
                break
        atualizar_usuarios(usuarios)
        
        print(f"\n {minutos} minutos registrados!")
    except:
        print("\nPor favor, digite apenas números!")
        pausar()
        return False
    
    pausar()
    return True