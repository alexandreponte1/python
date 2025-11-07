lista = ["Maria", "Alex", "Luiz",]
lista.append("João")

# lista_enumerada = enumerate(lista)
# print(next(lista_enumerada))

# print(type(lista_enumerada))

# print

# for item in lista_enumerada:
#     print(item)


# lista_enumerada = list(enumerate(lista))

# print(lista_enumerada)


for indice, nome in enumerate(lista):
    # print(f"\t{indice}, {nome}")
    print(indice, nome, lista[indice])