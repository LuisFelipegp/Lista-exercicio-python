numero = int(input("Digite um numero inteiro: "))

# Caso reste um valor da divisão é impar, do contrario é par
if numero % 2 == 0:
    print(numero, "é um número par pois nao resta numero apos a divisão")
else:
    print(numero, "é um número ímpar pois resta numero apos a divisao")