"""
Listas em python
Tipo list - Mutável
Suporta varios valores de qualquer tipo
conhecimentos reutilizaveis - indices fatiamento 
metodos úteis: append, insert, pop, del, clear, extend, + 
"""


# #       01234
# #      -54321

# string = "ABCDE" # 5 caracteres
# # print(lista, type(lista))
# #         0     1               2       3   4
# #        -5    -4              -3      -2  -1
# lista = [123, True, "Alexandre Ponte", 1.2, []]
# # print(lista[2].upper(), type(lista[2]))

# lista[-3] = "Maria"
# print(lista)
# print(lista[2], type(lista[2]))



lista = [10, 20, 30, 40]
# print(lista[2])

# numero = lista[2]

# print(numero)

# lista[2] = 300
# # print(lista[2])
# del lista[2]
# print(lista)
# print(lista[2])


# lista.append(50)
# lista.pop()
# lista.append(70)
# ultimo_valor = lista.pop(3)
# lista.append(60)
# print(lista, "removido, ", ultimo_valor)

#        0   1   2   3
# lista = [10, 20, 30, 40]
# lista.append("Alexandre")
# nome = lista.pop()
# lista.append(1233)
# del lista[-1]
# # lista.clear()
# lista.insert(100, 5)
# print(lista[4])
# print(lista)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
print(lista_c)

lista_d = lista_a.extend(lista_b)

print(lista_a)

lista_d = lista_a

print(lista_d)





