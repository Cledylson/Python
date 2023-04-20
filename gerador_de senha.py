import random
import string

# Define o tamanho da senha
tamanho_senha = int(input("Coloque o tamanho da senha ex:8,10... "))  # ou 10, dependendo do que você precisa

# Define os caracteres que serão usados na senha
caracteres = string.ascii_letters + string.digits

# Gera a senha aleatória
senha = ''.join(random.choice(caracteres) for i in range(tamanho_senha))

# Imprime a senha gerada
print("Senha gerada e arquivada: ", senha)

# Armazena a senha em um arquivo
with open("senha.txt", "w") as arquivo:
    arquivo.write(senha)
