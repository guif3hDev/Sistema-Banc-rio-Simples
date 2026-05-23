from utils import Fore, datetime
from dados import usuarios, sessao
from arquivos import salvar_usuarios
from usuarios import usuario_deslogado

# 1 - Depositar
def depositar():

    if usuario_deslogado():
        return

    try:
        deposito = float(input("Quanto deseja depositar: R$"))

        if deposito <= 0:
            print(Fore.RED + "Digite um valor válido!")
            return

        usuarios[sessao["usuario_atual"]]["saldo"] += deposito

        data = datetime.now().strftime("%d/%m/%Y %H:%M")

        usuarios[sessao["usuario_atual"]]["extrato"].append(
            f"[{data}] DEPÓSITO: + R${deposito:.2f}"
        )

        print(Fore.GREEN + "Depósito realizado!")

        print(
            Fore.YELLOW +
            f"Saldo atual: "
            f"R${usuarios[sessao['usuario_atual']]['saldo']:.2f}"
        )

        salvar_usuarios()

    except ValueError:
        print(Fore.RED + "Digite apenas números!")


# 2 - Sacar
def sacar():

    if usuario_deslogado():
        return

    try:
        saque = float(input("Quanto deseja sacar: R$"))

        if saque <= 0:
            print(Fore.RED + "Digite um valor válido!")
            return

        if saque > usuarios[sessao["usuario_atual"]]["saldo"]:
            print(Fore.RED + "Saldo insuficiente!")
            return

        usuarios[sessao["usuario_atual"]]["saldo"] -= saque

        data = datetime.now().strftime("%d/%m/%Y %H:%M")

        usuarios[sessao["usuario_atual"]]["extrato"].append(
            f"[{data}] SAQUE: - R${saque:.2f}"
        )

        print(Fore.GREEN + "Saque realizado!")

        print(
            Fore.YELLOW +
            f"Saldo atual: "
            f"R${usuarios[sessao['usuario_atual']]['saldo']:.2f}"
        )

        salvar_usuarios()

    except ValueError:
        print(Fore.RED + "Digite apenas números!")


# 3 - Ver saldo
def ver_saldo():

    if usuario_deslogado():
        return

    print(
        Fore.GREEN +
        f"SALDO: "
        f"R${usuarios[sessao['usuario_atual']]['saldo']:.2f}"
    )


# 4 - Ver extrato
def ver_extrato():

    if usuario_deslogado():
        return

    if not usuarios[sessao["usuario_atual"]]["extrato"]:
        print(Fore.RED + "Não há movimentações!")

    else:

        for item in usuarios[sessao["usuario_atual"]]["extrato"]:
            print(item)

# 5 - Transferência
def transferencia():

    if usuario_deslogado():
        return

    pessoa_desejada = input(
        "Digite o email que deseja transferir: "
    ).strip()

    try:

        valor = float(input("Digite o valor desejado: "))

        if valor <= 0:
            print(Fore.RED + "Digite um valor válido!")
            return

        if (
            pessoa_desejada in usuarios and
            pessoa_desejada != sessao["usuario_atual"]
        ):

            if usuarios[sessao["usuario_atual"]]["saldo"] < valor:
                print(Fore.RED + "Saldo insuficiente!")
                return

            atualizar_saldo(valor, pessoa_desejada)

            data = datetime.now().strftime("%d/%m/%Y %H:%M")

            registrar_extrato(valor, data, pessoa_desejada)

            print(Fore.GREEN + "Transferência realizada!")

            print(
                Fore.YELLOW +
                f"Saldo atual: "
                f"R${usuarios[sessao['usuario_atual']]['saldo']:.2f}"
            )

            salvar_usuarios()

        else:

            print(Fore.RED + "Usuário não encontrado ou inválido!")

    except ValueError:

        print(Fore.RED + "Digite apenas números!")

def registrar_extrato(valor,data,pessoa_desejada):
            
    usuarios[sessao["usuario_atual"]]["extrato"].append(
        f"[{data}] TRANSFERÊNCIA: - R${valor:.2f}"
        )

    usuarios[pessoa_desejada]["extrato"].append(
            f"[{data}] RECEBIDO: + R${valor:.2f}"
       )

def atualizar_saldo(valor, pessoa_desejada):
    usuarios[sessao["usuario_atual"]]["saldo"] -= valor

    usuarios[pessoa_desejada]["saldo"] += valor 