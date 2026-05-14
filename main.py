import os

for nome_arquivo in ["videos.txt", "usuarios.txt", "curtidas.txt", "favoritos.txt"]:
    if not os.path.exists(nome_arquivo):
        open(nome_arquivo, "w", encoding="utf-8").close()

from auth    import cadastrar_usuario, login_usuario
from usuario import buscar_video, curtir_descurtir, gerenciar_favoritos


def exibir_banner():
    print("\n" + "=" * 55)
    print("          ▶  F E I t v  — Plataforma de Vídeos")
    print("=" * 55)



def menu_principal():
    while True:
        exibir_banner()
        print("1. Login")
        print("2. Cadastrar novo usuário")
        print("0. Sair")

        opcao = input("\nOpção: ").strip()

        if opcao == "1":
            usuario = login_usuario()
            if usuario:
                menu_usuario(usuario)

        elif opcao == "2":
            cadastrar_usuario()

        elif opcao == "0":
            print("\nAté logo!")
            break

        else:
            print("Opção inválida.")


def menu_usuario(usuario):
    while True:
        print(f"\n=== Menu — {usuario} ===")
        print("1. Buscar")
        print("2. Curtir / Descurtir vídeo")
        print("3. Gerenciar favoritos")
        print("0. Logout")

        opcao = input("Opção: ").strip()

        if opcao == "1":
            buscar_video(usuario)
        elif opcao == "2":
            curtir_descurtir(usuario)
        elif opcao == "3":
            gerenciar_favoritos(usuario)
        elif opcao == "0":
            print("Logout realizado.")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu_principal()
