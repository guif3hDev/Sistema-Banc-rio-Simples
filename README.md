# Sistema Bancário em Python

Um sistema bancário simples feito em Python no terminal, com funcionalidades de cadastro, login, depósito, saque, saldo, extrato e salvamento em arquivo `.txt`.

---

# Funcionalidades

- Cadastro de usuários
- Login de usuário
- Depósito
- Saque
- Ver saldo
- Ver extrato
- Salvamento do extrato em `.txt`
- Data e hora das movimentações
- Validações de entrada
- Tratamento de erros com `try/except`
- Sistema de logout

---

# Estrutura do Projeto

O sistema funciona utilizando:

- Funções
- Dicionários
- Listas
- Estruturas de repetição
- Estruturas condicionais
- Manipulação de arquivos
- Tratamento de exceções

---

# Estrutura dos Usuários

Cada usuário possui:

```python
usuarios[email] = {
    "senha": senha,
    "saldo": 0,
    "extrato": []
}
```

## Explicação

- `senha` → senha do usuário
- `saldo` → saldo individual
- `extrato` → lista com movimentações do usuário

---

# Como o Login Funciona

Quando o usuário faz login:

```python
usuario_atual = email_login
```

O sistema salva quem está logado atualmente.

Depois disso, todas as funções acessam os dados usando:

```python
usuarios[usuario_atual]
```

Exemplo:

```python
usuarios[usuario_atual]["saldo"]
```

Isso permite que cada usuário tenha:

- saldo próprio
- extrato próprio
- informações separadas

---

# Sistema de Depósito

O depósito:

1. Verifica se o usuário está logado
2. Verifica se o valor é válido
3. Soma o valor ao saldo
4. Salva no extrato
5. Salva no arquivo `.txt`

Exemplo:

```python
usuarios[usuario_atual]["saldo"] += deposito
```

---

# Sistema de Saque

O saque:

1. Verifica login
2. Verifica saldo suficiente
3. Impede valores negativos
4. Remove o valor do saldo
5. Salva no extrato

Exemplo:

```python
usuarios[usuario_atual]["saldo"] -= saque
```

---

# Sistema de Extrato

As movimentações ficam armazenadas em uma lista:

```python
"extrato": []
```

Cada movimentação salva:

- tipo da operação
- valor
- data
- hora

Exemplo:

```python
[13/05/2026 14:30] DEPÓSITO: + R$100.00
```

---

# Salvamento em Arquivo `.txt`

O sistema salva o extrato automaticamente usando:

```python
with open("extrato.txt", "w", encoding="utf-8")
```

---

# Tratamento de Erros

O projeto utiliza `try/except` para evitar erros do programa.

Exemplo:

```python
try:
    deposito = float(input())
except ValueError:
    print("Digite apenas números!")
```

---

# Aprendizados no Projeto

Durante o desenvolvimento pratiquei:

- lógica de programação
- organização de código
- funções
- dicionários aninhados
- manipulação de listas
- tratamento de erros
- persistência de dados
- estruturação de sistemas maiores

---

# Melhorias Futuras

- Interface gráfica
- Banco de dados
- Criptografia de senha
- Histórico individual em arquivos separados
- Interface web com Flask/Django

---

# Tecnologias Utilizadas

- Python
- Colorama
- Datetime

---

Projeto desenvolvido para estudos e prática de lógica de programação em Python.
