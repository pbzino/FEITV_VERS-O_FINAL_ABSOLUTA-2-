
from arquivo_utils import (
    carregar_videos, salvar_videos,
    carregar_curtidas, salvar_curtidas,
    carregar_favoritos, salvar_favoritos
)


# ──────────────────────────────────────────────
#  EXIBIÇÃO
# ──────────────────────────────────────────────

def exibir_video(video, usuario=None, curtidas=None):
    """Imprime as informações de um vídeo formatado."""
    curtiu = ""
    if usuario and curtidas:
        if usuario in curtidas and video["id"] in curtidas[usuario]:
            curtiu = " ♥ (você curtiu)"
    print("-" * 55)
    print(f"  ID       : {video['id']}")
    print(f"  Título   : {video['titulo']}")
    print(f"  Diretor  : {video['diretor']}")
    print(f"  Ano      : {video['ano']}")
    print(f"  Gênero   : {video['genero']}")
    print(f"  Duração  : {video['duracao']} min")
    print(f"  Sinopse  : {video['sinopse']}")
    print(f"  Curtidas : {video['total_curtidas']}{curtiu}")
    print("-" * 55)


# ──────────────────────────────────────────────
#  BUSCA
# ──────────────────────────────────────────────

def buscar_video(usuario):
    """Busca vídeos pelo nome (busca parcial, ignora maiúsculas/minúsculas)."""
    print("\n--- BUSCAR VÍDEO ---")
    termo = input("Digite o nome do vídeo: ").strip().lower()
    if not termo:
        print("Termo de busca inválido.")
        return

    videos   = carregar_videos()
    curtidas = carregar_curtidas()
    encontrados = [v for v in videos if termo in v["titulo"].lower()]

    if not encontrados:
        print("Nenhum vídeo encontrado.")
        return

    print(f"\n{len(encontrados)} resultado(s) encontrado(s):\n")
    for v in encontrados:
        exibir_video(v, usuario, curtidas)


def curtir_descurtir(usuario):
    """Permite ao usuário curtir ou descurtir um vídeo pelo ID."""
    print("\n--- CURTIR / DESCURTIR VÍDEO ---")
    videos   = carregar_videos()
    curtidas = carregar_curtidas()

    try:
        id_video = int(input("Digite o ID do vídeo: ").strip())
    except ValueError:
        print("ID inválido.")
        return

    # Localiza o vídeo na lista
    video = next((v for v in videos if v["id"] == id_video), None)
    if video is None:
        print("Vídeo não encontrado.")
        return

    if usuario not in curtidas:
        curtidas[usuario] = set()

    if id_video in curtidas[usuario]:
        # Descurtir
        curtidas[usuario].remove(id_video)
        video["total_curtidas"] -= 1
        print(f"Você descurtiu '{video['titulo']}'.")
    else:
        # Curtir
        curtidas[usuario].add(id_video)
        video["total_curtidas"] += 1
        print(f"Você curtiu '{video['titulo']}'!")

    salvar_curtidas(curtidas)
    salvar_videos(videos)


def gerenciar_favoritos(usuario):
    """Menu de gerenciamento de favoritos do usuário."""
    while True:
        print("\n--- GERENCIAR FAVORITOS ---")
        print("1. Criar nova lista de favoritos")
        print("2. Ver minhas listas de favoritos")
        print("3. Adicionar vídeo à lista de favoritos")
        print("4. Remover vídeo da lista de favoritos")
        print("5. Editar nome da lista de favoritos")
        print("6. Excluir lista de favoritos")
        print("0. Voltar")

        opcao = input("Opção: ").strip()

        if opcao == "1":
            criar_lista_favoritos(usuario)
        elif opcao == "2":
            listar_favoritos(usuario)
        elif opcao == "3":
            adicionar_video_favoritos(usuario)
        elif opcao == "4":
            remover_video_favoritos(usuario)
        elif opcao == "5":
            editar_nome_lista_favoritos(usuario)
        elif opcao == "6":
            excluir_lista_favoritos(usuario)
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


def criar_lista_favoritos(usuario):
    """Cria uma nova lista de favoritos com nome único para o usuário."""
    favoritos = carregar_favoritos()
    nome = input("Nome da nova lista de favoritos: ").strip()
    if not nome:
        print("Nome inválido.")
        return

    if usuario not in favoritos:
        favoritos[usuario] = {}

    if nome in favoritos[usuario]:
        print("Já existe uma lista de favoritos com esse nome.")
        return

    favoritos[usuario][nome] = []
    salvar_favoritos(favoritos)
    print(f"Lista de favoritos '{nome}' criada com sucesso!")


def listar_favoritos(usuario):
    favoritos = carregar_favoritos()
    videos    = carregar_videos()

    if usuario not in favoritos or not favoritos[usuario]:
        print("Você não tem listas de favoritos ainda.")
        return

    videos_dict = {v["id"]: v for v in videos}

    for nome, ids in favoritos[usuario].items():
        print(f"\n⭐ {nome} ({len(ids)} vídeo(s))")
        if not ids:
            print("   (lista vazia)")
        else:
            for id_v in ids:
                if id_v in videos_dict:
                    print(f"   [{id_v}] {videos_dict[id_v]['titulo']}")
                else:
                    print(f"   [{id_v}] (vídeo removido)")


def adicionar_video_favoritos(usuario):
    favoritos = carregar_favoritos()
    videos    = carregar_videos()

    if usuario not in favoritos or not favoritos[usuario]:
        print("Você não tem listas de favoritos. Crie uma primeiro.")
        return

    listar_favoritos(usuario)
    nome = input("\nNome da lista de favoritos: ").strip()

    if nome not in favoritos[usuario]:
        print("Lista de favoritos não encontrada.")
        return

    try:
        id_video = int(input("ID do vídeo a adicionar: ").strip())
    except ValueError:
        print("ID inválido.")
        return

    video = next((v for v in videos if v["id"] == id_video), None)
    if video is None:
        print("Vídeo não encontrado.")
        return

    if id_video in favoritos[usuario][nome]:
        print("Este vídeo já está nessa lista de favoritos.")
        return

    favoritos[usuario][nome].append(id_video)
    salvar_favoritos(favoritos)
    print(f"'{video['titulo']}' adicionado à lista '{nome}'.")


def remover_video_favoritos(usuario):
    favoritos = carregar_favoritos()

    if usuario not in favoritos or not favoritos[usuario]:
        print("Você não tem listas de favoritos.")
        return

    listar_favoritos(usuario)
    nome = input("\nNome da lista de favoritos: ").strip()

    if nome not in favoritos[usuario]:
        print("Lista de favoritos não encontrada.")
        return

    try:
        id_video = int(input("ID do vídeo a remover: ").strip())
    except ValueError:
        print("ID inválido.")
        return

    if id_video not in favoritos[usuario][nome]:
        print("Este vídeo não está nessa lista de favoritos.")
        return

    favoritos[usuario][nome].remove(id_video)
    salvar_favoritos(favoritos)
    print("Vídeo removido da lista de favoritos.")


def editar_nome_lista_favoritos(usuario):
    favoritos = carregar_favoritos()

    if usuario not in favoritos or not favoritos[usuario]:
        print("Você não tem listas de favoritos.")
        return

    listar_favoritos(usuario)
    nome_antigo = input("\nNome da lista de favoritos a renomear: ").strip()

    if nome_antigo not in favoritos[usuario]:
        print("Lista de favoritos não encontrada.")
        return

    nome_novo = input("Novo nome: ").strip()
    if not nome_novo:
        print("Nome inválido.")
        return

    if nome_novo in favoritos[usuario]:
        print("Já existe uma lista de favoritos com esse nome.")
        return

    favoritos[usuario][nome_novo] = favoritos[usuario].pop(nome_antigo)
    salvar_favoritos(favoritos)
    print(f"Lista de favoritos renomeada para '{nome_novo}'.")


def excluir_lista_favoritos(usuario):
    favoritos = carregar_favoritos()

    if usuario not in favoritos or not favoritos[usuario]:
        print("Você não tem listas de favoritos.")
        return

    listar_favoritos(usuario)
    nome = input("\nNome da lista de favoritos a excluir: ").strip()

    if nome not in favoritos[usuario]:
        print("Lista de favoritos não encontrada.")
        return

    confirmacao = input(f"Tem certeza que deseja excluir '{nome}'? (s/n): ").strip().lower()
    if confirmacao != "s":
        print("Operação cancelada.")
        return

    del favoritos[usuario][nome]
    salvar_favoritos(favoritos)
    print(f"Lista de favoritos '{nome}' excluída.")
