import os

CAMINHO_VIDEOS    = "videos.txt"
CAMINHO_USUARIOS  = "usuarios.txt"
CAMINHO_CURTIDAS  = "curtidas.txt"
CAMINHO_FAVORITOS = "favoritos.txt"


def carregar_videos():
    videos = []
    if not os.path.exists(CAMINHO_VIDEOS):
        return videos
    with open(CAMINHO_VIDEOS, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue
            partes = linha.split("|")
            if len(partes) < 8:
                continue
            videos.append({
                "id":            int(partes[0]),
                "titulo":        partes[1],
                "diretor":       partes[2],
                "ano":           partes[3],
                "genero":        partes[4],
                "duracao":       partes[5],
                "sinopse":       partes[6],
                "total_curtidas": int(partes[7])
            })
    return videos


def salvar_videos(videos):
    with open(CAMINHO_VIDEOS, "w", encoding="utf-8") as f:
        for v in videos:
            linha = (
                f"{v['id']}|{v['titulo']}|{v['diretor']}|{v['ano']}|"
                f"{v['genero']}|{v['duracao']}|{v['sinopse']}|{v['total_curtidas']}\n"
            )
            f.write(linha)


def proximo_id_video():
    videos = carregar_videos()
    if not videos:
        return 1
    return max(v["id"] for v in videos) + 1


def carregar_usuarios():
    usuarios = {}
    if not os.path.exists(CAMINHO_USUARIOS):
        return usuarios
    with open(CAMINHO_USUARIOS, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue
            partes = linha.split("|")
            if len(partes) == 2:
                usuarios[partes[0]] = partes[1]
    return usuarios


def salvar_usuarios(usuarios):
    with open(CAMINHO_USUARIOS, "w", encoding="utf-8") as f:
        for usuario, senha in usuarios.items():
            f.write(f"{usuario}|{senha}\n")



def carregar_curtidas():
    curtidas = {}
    if not os.path.exists(CAMINHO_CURTIDAS):
        return curtidas
    with open(CAMINHO_CURTIDAS, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue
            partes = linha.split("|")
            if len(partes) == 2:
                usuario  = partes[0]
                id_video = int(partes[1])
                if usuario not in curtidas:
                    curtidas[usuario] = set()
                curtidas[usuario].add(id_video)
    return curtidas


def salvar_curtidas(curtidas):
    with open(CAMINHO_CURTIDAS, "w", encoding="utf-8") as f:
        for usuario, ids in curtidas.items():
            for id_video in ids:
                f.write(f"{usuario}|{id_video}\n")



def carregar_favoritos():
    favoritos = {}
    if not os.path.exists(CAMINHO_FAVORITOS):
        return favoritos
    with open(CAMINHO_FAVORITOS, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue
            partes = linha.split("|")
            if len(partes) < 2:
                continue
            usuario = partes[0]
            nome_lista = partes[1]
            ids_str = partes[2] if len(partes) > 2 else ""

            if usuario not in favoritos:
                favoritos[usuario] = {}

            if ids_str:
                ids = [int(x) for x in ids_str.split(",") if x]
            else:
                ids = []

            favoritos[usuario][nome_lista] = ids
    return favoritos


def salvar_favoritos(favoritos):
    with open(CAMINHO_FAVORITOS, "w", encoding="utf-8") as f:
        for usuario, listas in favoritos.items():
            for nome_lista, ids in listas.items():
                ids_str = ",".join(str(i) for i in ids)
                f.write(f"{usuario}|{nome_lista}|{ids_str}\n")
