from colorama import Fore
from datetime import datetime

# data = datetime.now().strftime("%d/%m/%Y %H:%M") Esse comando serve para marcar a hora e a data exata - uso junto da função salvar_extrato
saldo = 0 # Aqui eu crio um contador para sempre salvar os depositos e os saques - IMPORTANTE PARA AS PRÓXIMAS LÓGICAS ONDE EU TENHO QUE SALVAR UM VALOR QUE ALTERA!
extrato = [] # Aqui eu crio uma lista para salvar as transações feitas, e uso um for para percorrer a lista e me mostrar em forma listada!

# 1 - Depositar
def depositar():
    global saldo
    
    try:
        deposito = float(input("Quanto deseja depositar: R$"))

        if deposito <= 0:
            print("Digite um valor válido!")
            return
        
        saldo += deposito
        print(Fore.GREEN + "Deposito realizado!")
        print(Fore.YELLOW + f"Saldo ATUAL: R${saldo:.2f}")

        data = datetime.now().strftime("%d/%m/%Y %H:%M")
        extrato.append(f"[{data}] DEPÓSITO: + R${deposito:.2f}") # Aqui anteriormente eu coloquei para salvar o saldo, mas o correto é salvar o deposito!
        salvar_extrato()
    
    except ValueError:
        print(Fore.RED + "Digite apenas números!")

# 2 - Sacar
def sacar():
    global saldo

    try:
        saque = float(input("Quanto deseja sacar: "))

        if saque > saldo:
            print(Fore.RED + "Saldo insuficiente!") # Aqui eu deveria ter verificado se o saque é maior que o saldo, pois sem isso dá para sacar negativo!
            return
        
        elif saque <= 0:
            print(Fore.RED + "Digite um valor válido!")
            return
        
        saldo -= saque
        
        data = datetime.now().strftime("%d/%m/%Y %H:%M")
        extrato.append(f"[{data}] SAQUE: - R${saque:.2f}") # Aqui eu errei a mesma coisa na função depositar! Mas consertei.
        salvar_extrato()
        print(Fore.GREEN + "Saque realizado!")
        print(Fore.YELLOW + f"Saldo ATUAL: R${saldo:.2f}")
    
    except ValueError:
        print(Fore.RED + "Digite apenas números!")

# 3 - Ver saldo
def ver_saldo():
    print(Fore.GREEN + f"SALDO: R${saldo:.2f}")


# 4 - Ver extrato
def ver_extrato():
    if not extrato:
        print(Fore.RED + "Não há movimentações!")

    else:
        for ver in extrato:
            print(f"{ver}")
        
menu = {
    "1" : depositar,
    "2" : sacar,
    "3" : ver_saldo,
    "4" : ver_extrato, 
    }

def salvar_extrato():
    with open("extrato.txt", "w", encoding="utf-8") as arquivo:
        for item in extrato:
            arquivo.write(f"{item}\n")
    
# 5 - Sair
def menu_principal():

    while True:
        print(Fore.WHITE + """
=== BANCO PYTHON ===
\n1 - Depositar
2 - Sacar
3 - Ver saldo
4 - Ver extrato
5 - Sair
    """)
        
        opcao = input(Fore.BLUE + "Escolha uma opção: ")

        if opcao in menu:
            menu[opcao]()

        elif opcao == "5":
            print(Fore.YELLOW + "Saindo...")
            break

        else:
            print(Fore.RED + "Opção inválida!")

menu_principal()