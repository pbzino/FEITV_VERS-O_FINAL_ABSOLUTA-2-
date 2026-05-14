from arquivo_utils import carregar_usuarios, salvar_usuarios



def cadastrar_usuario():
    print("\n--- CADASTRO DE USUÁRIO ---")
    usuarios = carregar_usuarios()

    usuario = input("Digite um nome de usuário: ").strip()
    if not usuario:
        print("Nome de usuário inválido.")
        return False
    if usuario in usuarios:
        print("Nome de usuário já cadastrado.")
        return False

    senha = input("Digite uma senha: ").strip()
    if not senha:
        print("Senha inválida.")
        return False

    confirmacao = input("Confirme a senha: ").strip()
    if senha != confirmacao:
        print("As senhas não coincidem.")
        return False

    usuarios[usuario] = senha
    salvar_usuarios(usuarios)
    print(f"Usuário '{usuario}' cadastrado com sucesso!")
    return True


def login_usuario():
    
    print("\n--- LOGIN ---")
    usuario = input("Usuário: ").strip()
    senha   = input("Senha: ").strip()

    usuarios = carregar_usuarios()
    if usuario in usuarios and usuarios[usuario] == senha:
        print(f"Bem-vindo, {usuario}!")
        return usuario

    print("Usuário ou senha incorretos.")
    return None
