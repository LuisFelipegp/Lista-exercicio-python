palavra = input("Digite uma palavra: ")

# Verifica se a palavra é um palíndromo
if palavra == palavra[::-1]: # sintaxe para inverter a palavra
    print("A palavra é um palíndromo!")
else:
    print("A palavra não é um palíndromo.")