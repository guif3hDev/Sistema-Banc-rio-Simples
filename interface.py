import tkinter as tk
from tkinter import messagebox

from dados import usuarios, sessao

from arquivos import (
    carregar_usuarios,
    salvar_usuarios
)

from usuarios import (
    login_usuario,
    cadastrar_usuario
)

# ==========================================
# CARREGAR USUÁRIOS
# ==========================================

carregar_usuarios()


# ==========================================
# MOSTRAR SALDO
# ==========================================

def mostrar_saldo():

    saldo = usuarios[sessao["usuario_atual"]]["saldo"]

    messagebox.showinfo(
        "Saldo",
        f"Seu saldo é R${saldo:.2f}"
    )


# ==========================================
# DEPOSITAR
# ==========================================

def depositar():

    janela_deposito = tk.Toplevel(janela)

    janela_deposito.title("Depositar")

    janela_deposito.geometry("300x200")

    titulo = tk.Label(
        janela_deposito,
        text="DEPÓSITO",
        font=("Arial", 14, "bold")
    )

    titulo.pack(pady=20)

    entry_valor = tk.Entry(
        janela_deposito,
        width=25
    )

    entry_valor.pack(pady=10)

    def confirmar_deposito():

        try:

            valor = float(entry_valor.get())

            if valor <= 0:

                messagebox.showerror(
                    "Erro",
                    "Digite um valor válido!"
                )

                return

            usuarios[sessao["usuario_atual"]]["saldo"] += valor

            salvar_usuarios()

            messagebox.showinfo(
                "Sucesso",
                f"Depósito de R${valor:.2f} realizado!"
            )

            janela_deposito.destroy()

        except ValueError:

            messagebox.showerror(
                "Erro",
                "Digite apenas números!"
            )

    botao_confirmar = tk.Button(
        janela_deposito,
        text="Confirmar depósito",
        command=confirmar_deposito
    )

    botao_confirmar.pack(pady=20)


# ==========================================
# SACAR
# ==========================================

def sacar():

    janela_saque = tk.Toplevel(janela)

    janela_saque.title("Sacar")

    janela_saque.geometry("300x200")

    titulo = tk.Label(
        janela_saque,
        text="SAQUE",
        font=("Arial", 14, "bold")
    )

    titulo.pack(pady=20)

    entry_valor = tk.Entry(
        janela_saque,
        width=25
    )

    entry_valor.pack(pady=10)

    def confirmar_saque():

        try:

            valor = float(entry_valor.get())

            if valor <= 0:

                messagebox.showerror(
                    "Erro",
                    "Digite um valor válido!"
                )

                return

            saldo = usuarios[sessao["usuario_atual"]]["saldo"]

            if valor > saldo:

                messagebox.showerror(
                    "Erro",
                    "Saldo insuficiente!"
                )

                return

            usuarios[sessao["usuario_atual"]]["saldo"] -= valor

            salvar_usuarios()

            messagebox.showinfo(
                "Sucesso",
                f"Saque de R${valor:.2f} realizado!"
            )

            janela_saque.destroy()

        except ValueError:

            messagebox.showerror(
                "Erro",
                "Digite apenas números!"
            )

    botao_confirmar = tk.Button(
        janela_saque,
        text="Confirmar saque",
        command=confirmar_saque
    )

    botao_confirmar.pack(pady=20)


# ==========================================
# ABRIR MENU
# ==========================================

def abrir_menu():

    nova_janela = tk.Toplevel(janela)

    nova_janela.title("MENU BANCO")

    nova_janela.geometry("400x300")

    # --------------------------------------
    # FECHAR MENU
    # --------------------------------------

    def fechar_menu():

        nova_janela.destroy()

        janela.deiconify()

    nova_janela.protocol(
        "WM_DELETE_WINDOW",
        fechar_menu
    )

    # --------------------------------------
    # TÍTULO
    # --------------------------------------

    titulo = tk.Label(
        nova_janela,
        text="MENU PRINCIPAL",
        font=("Arial", 16, "bold")
    )

    titulo.pack(pady=20)

    # --------------------------------------
    # BOTÃO SALDO
    # --------------------------------------

    botao_saldo = tk.Button(
        nova_janela,
        text="Ver saldo",
        width=20,
        command=mostrar_saldo
    )

    botao_saldo.pack(pady=10)

    # --------------------------------------
    # BOTÃO SACAR
    # --------------------------------------

    botao_sacar = tk.Button(
        nova_janela,
        text="Sacar",
        width=20,
        command=sacar
    )

    botao_sacar.pack(pady=10)

    # --------------------------------------
    # BOTÃO DEPOSITAR
    # --------------------------------------

    botao_depositar = tk.Button(
        nova_janela,
        text="Depositar",
        width=20,
        command=depositar
    )

    botao_depositar.pack(pady=10)


# ==========================================
# CADASTRO
# ==========================================

def fazer_cadastro():

    email = entry_email.get()

    senha = entry_senha.get()

    sucesso = cadastrar_usuario(email, senha)

    if sucesso:

        messagebox.showinfo(
            "Sucesso",
            "Usuário cadastrado!"
        )

        entry_email.delete(0, tk.END)

        entry_senha.delete(0, tk.END)

    else:

        messagebox.showerror(
            "Erro",
            "Usuário já existe!"
        )


# ==========================================
# LOGIN
# ==========================================

def fazer_login():

    email = entry_email.get()

    senha = entry_senha.get()

    sucesso = login_usuario(email, senha)

    if sucesso:

        messagebox.showinfo(
            "Sucesso",
            "Login realizado com sucesso!"
        )

        entry_email.delete(0, tk.END)

        entry_senha.delete(0, tk.END)

        janela.withdraw()

        abrir_menu()

    else:

        messagebox.showerror(
            "Erro",
            "Email ou senha inválidos!"
        )


# ==========================================
# JANELA PRINCIPAL
# ==========================================

janela = tk.Tk()

janela.title("BANCO PYTHON")

janela.geometry("400x300")

janela.configure(
    padx=20,
    pady=20
)


# ==========================================
# TÍTULO
# ==========================================

titulo = tk.Label(
    janela,
    text="LOGIN BANCO PYTHON",
    font=("Arial", 16, "bold")
)

titulo.pack(pady=20)


# ==========================================
# EMAIL
# ==========================================

label_email = tk.Label(
    janela,
    text="Email"
)

label_email.pack()

entry_email = tk.Entry(
    janela,
    width=30
)

entry_email.pack(pady=5)


# ==========================================
# SENHA
# ==========================================

label_senha = tk.Label(
    janela,
    text="Senha"
)

label_senha.pack()

entry_senha = tk.Entry(
    janela,
    width=30,
    show="*"
)

entry_senha.pack(pady=5)


# ==========================================
# BOTÃO LOGIN
# ==========================================

botao_login = tk.Button(
    janela,
    text="Entrar",
    width=15,
    command=fazer_login
)

botao_login.pack(pady=20)


# ==========================================
# BOTÃO CADASTRO
# ==========================================

botao_cadastro = tk.Button(
    janela,
    text="Cadastrar",
    width=15,
    command=fazer_cadastro
)

botao_cadastro.pack(pady=5)


# ==========================================
# LOOP PRINCIPAL
# ==========================================
def iniciar_interface():
    janela.mainloop()