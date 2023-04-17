import random
import string

def generate_password(length):
    # definindo caracteres que podem ser usado
    characters = string.ascii_letters + string.digits + string.punctuation

    # cria uma senha aleatória usando os caracteres disponíveis
    password = ''.join(random.choice(characters) for i in range(length))

    return password

# pede ao usuário para digitar o comprimento desejado da senha
length = int(input("Digite o comprimento da senha desejada: "))

# gera uma nova senha aleatória
password = generate_password(length)

# imprime a senha gerada
print("Sua nova senha aleatória é: ", password)