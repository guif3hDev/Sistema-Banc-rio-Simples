from utils import Fore
from dados import usuarios, sessao
from arquivos import salvar_usuarios


# Função para cadastrar usuário
def cadastrar_usuario(email, senha):

    if email in usuarios:
        return False

    usuarios[email] = {
        "senha": senha,
        "saldo": 0,
        "extrato": []
    }

    salvar_usuarios()

    return True


def login_usuario(email, senha):

    if (
        email in usuarios and
        senha == usuarios[email]["senha"]
    ):

        sessao["logado"] = True
        sessao["usuario_atual"] = email

        return True

    return False


def logout_usuario():

    if not sessao["logado"]:
        print(Fore.RED + "Faça login primeiro!")
        return

    sessao["usuario_atual"] = None
    sessao["logado"] = False

    print(Fore.GREEN + "Logout realizado!")
    

def usuario_deslogado():

    if not sessao["logado"]:
        print(Fore.RED + "Faça login primeiro!")
        return True

    return False