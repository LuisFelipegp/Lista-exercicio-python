with open("names.txt", "r") as f:
    nomes = f.read().splitlines()

contador_nomes = {}
for nome in nomes:
    if nome in contador_nomes:
        contador_nomes[nome] += 1
    else:
        contador_nomes[nome] = 1

for nome, contador in contador_nomes.items():
    print(f"{nome}: {contador}")