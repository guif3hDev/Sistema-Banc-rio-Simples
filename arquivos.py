import json
from dados import usuarios

# Função responsável por salvar os usuários no arquivo JSON
def salvar_usuarios():
    with open("usuarios.json", "w", encoding='utf-8') as arquivo:

        # json.dump converte dicionário Python para JSON
        json.dump(
            usuarios,
            arquivo,
            indent=4,
            ensure_ascii=False
        )

# Funçaõ responsável por carregar usuários do JSON
def carregar_usuarios():

    global usuarios

    try:

        # "r" = leitura
        with open("usuarios.json", "r", encoding='utf-8') as arquivo:
            
            # json.load transforma JSON em dicionário Python
            dados = json.load(arquivo)

            # Atualiza o dicionário usuarios
            usuarios.update(dados)
    
    # Caso o arquivo não exista ainda
    except FileNotFoundError:
        print("Arquivo JSON ainda não existe.")