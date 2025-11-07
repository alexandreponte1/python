"""
for in com listas
"""

lista = ["Maria", "Alex", "Luiz",]

# for letra in "ABC":
#     print(letra)

contador = 0
lista.append("Alexandre")
indices = range(len(lista))

# for nome in lista:
#     print(nome, contador)
#     contador += 1


print(indices)
for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
