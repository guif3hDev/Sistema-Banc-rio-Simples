from colorama import Fore # type: ignore
from datetime import datetime

# Aqui eu crio um dicionário para armazenar todos os usuários cadastrados
# Cada usuário terá:
# senha, saldo e extrato próprio
usuarios = {}

# Variável de controle:
# False = usuário não está logado
# True = usuário logado
logado = False

# Aqui eu salvo qual usuário fez login
# Exemplo: "gui@email.com"
usuario_atual = None


# 1 - Depositar
def depositar():

    # Se ninguém estiver logado, bloqueia a função
    if not logado:
        print(Fore.RED + "Faça login primeiro!")
        return  # Se o valor for inválido, o return encerra a função imediatamente para não continuar o depósito

    try:
        deposito = float(input("Quanto deseja depositar: R$"))

        # Verifica se o valor é menor ou igual a zero
        if deposito <= 0:
            print(Fore.RED + "Digite um valor válido!")
            return # return = encerra a função imediatamente

        # Aqui eu acesso o saldo do usuário logado
        # e adiciono o valor do depósito
        usuarios[usuario_atual]["saldo"] += deposito

        # Aqui eu pego a data e hora atual
        data = datetime.now().strftime("%d/%m/%Y %H:%M")

        # Aqui eu adiciono uma movimentação no extrato do usuário
        usuarios[usuario_atual]["extrato"].append(
            f"[{data}] DEPÓSITO: + R${deposito:.2f}"
        )

        # Salva o extrato no arquivo .txt
        salvar_extrato()

        print(Fore.GREEN + "Depósito realizado!")

        # Mostra o saldo atualizado do usuário
        print(
            Fore.YELLOW +
            f"Saldo atual: R${usuarios[usuario_atual]['saldo']:.2f}"
        )

    # Caso o usuário digite letras ao invés de números
    except ValueError:
        print(Fore.RED + "Digite apenas números!")


# 2 - Sacar
def sacar():

    # Bloqueia a função se não houver login
    if not logado:
        print(Fore.RED + "Faça login primeiro!")
        return # return = encerra a função imediatamente

    try:
        saque = float(input("Quanto deseja sacar: R$"))

        # Não permite saque zero ou negativo
        if saque <= 0:
            print(Fore.RED + "Digite um valor válido!")
            return # return = encerra a função imediatamente

        # Verifica se o usuário possui saldo suficiente
        if saque > usuarios[usuario_atual]["saldo"]:
            print(Fore.RED + "Saldo insuficiente!")
            return 

        # Remove o valor do saldo
        usuarios[usuario_atual]["saldo"] -= saque

        # Pega data e hora atual
        data = datetime.now().strftime("%d/%m/%Y %H:%M")

        # Salva a movimentação no extrato
        usuarios[usuario_atual]["extrato"].append(
            f"[{data}] SAQUE: - R${saque:.2f}"
        )

        # Salva o extrato no arquivo .txt
        salvar_extrato()

        print(Fore.GREEN + "Saque realizado!")

        # Mostra saldo atualizado
        print(
            Fore.YELLOW +
            f"Saldo atual: R${usuarios[usuario_atual]['saldo']:.2f}"
        )

    except ValueError:
        print(Fore.RED + "Digite apenas números!")


# 3 - Ver saldo
def ver_saldo():

    # Bloqueia caso não tenha login
    if not logado:
        print(Fore.RED + "Faça login primeiro!")
        return

    # Mostra o saldo do usuário atual
    print(
        Fore.GREEN +
        f"SALDO: R${usuarios[usuario_atual]['saldo']:.2f}"
    )


# 4 - Ver extrato
def ver_extrato():

    # Bloqueia se não houver login
    if not logado:
        print(Fore.RED + "Faça login primeiro!")
        return

    # Verifica se o extrato está vazio
    if not usuarios[usuario_atual]["extrato"]:
        print(Fore.RED + "Não há movimentações!")

    else:

        # Percorre toda a lista do extrato
        # e mostra cada movimentação
        for item in usuarios[usuario_atual]["extrato"]:
            print(item)


# Função responsável por salvar o extrato em um arquivo .txt
def salvar_extrato():

    # "w" = sobrescreve o arquivo inteiro
    # encoding="utf-8" permite usar caracteres especiais
    with open("extrato.txt", "w", encoding="utf-8") as arquivo:

        # Percorre o extrato do usuário logado
        for item in usuarios[usuario_atual]["extrato"]:

            # Escreve cada item em uma linha do arquivo
            arquivo.write(f"{item}\n")


# Função para cadastrar usuário
def cadastrar_usuario():

    email = input("Cadastre seu email: ")
    senha = input("Cadastre sua senha: ")

    # Verifica se o email já existe
    if email in usuarios:
        print(Fore.RED + "Usuário já cadastrado!")
        return

    # Aqui eu crio um dicionário dentro do dicionário usuarios
    # Cada usuário terá:
    # senha, saldo e extrato próprio
    usuarios[email] = {
        "senha": senha,
        "saldo": 0,
        "extrato": []
    }

    print(Fore.GREEN + "Usuário cadastrado com sucesso!")


# Função de login
def login_usuario():

    # "global" permite alterar variáveis fora da função
    global logado, usuario_atual

    # Quantidade máxima de tentativas
    tentativas = 3

    while tentativas > 0:

        email_login = input(Fore.WHITE + "Digite seu email: ")
        senha_login = input(Fore.WHITE + "Digite sua senha: ")

        # Verifica:
        # 1 - Se o email existe
        # 2 - Se a senha está correta
        if (
            email_login in usuarios and
            senha_login == usuarios[email_login]["senha"]
        ):

            print(Fore.GREEN + "Login realizado com sucesso!")

            # Marca que o usuário está logado
            logado = True

            # Salva quem é o usuário atual
            usuario_atual = email_login

            return

        else:

            # Remove uma tentativa
            tentativas -= 1

            print(
                Fore.RED +
                f"Senha incorreta. Tentativas restantes: {tentativas}"
            )

def logout_usuario():
    global logado, usuario_atual

    if not logado:
        print(Fore.RED + "Faça login primeiro!")
        return
    
    usuario_atual = None
    logado  = False

    print(Fore.GREEN + "Logout realizado!")
    
# Dicionário que liga opções do menu às funções
menu = {
    "1": cadastrar_usuario,
    "2": login_usuario,
    "3": depositar,
    "4": sacar,
    "5": ver_saldo,
    "6": ver_extrato,
    "7": logout_usuario
}


# Menu principal do sistema
def menu_principal():

    while True:

        print(Fore.WHITE + """
=== BANCO PYTHON ===

1 - Cadastrar usuário
2 - Login usuário
3 - Depositar
4 - Sacar
5 - Ver saldo
6 - Ver extrato
7 - logout
8 - Sair
""")

        opcao = input(Fore.BLUE + "Escolha uma opção: ")

        # Executa a função correspondente do dicionário menu
        if opcao in menu:
            menu[opcao]()

        # Fecha o programa
        elif opcao == "8":
            print(Fore.YELLOW + "Saindo...")
            break

        else:
            print(Fore.RED + "Opção inválida!")

# Inicia o sistema
menu_principal()
