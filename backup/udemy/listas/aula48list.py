"""
Cuidados com dados mutaveis
 = - copiando valor (imutáveis)
 = - aponta para o mesmo valor na memória(mutável)
"""

# nome = "Luiz"
# noutra_variavel = nome
# nome = "joao"
# print(nome)
# print(noutra_variavel)

lista_a = ["Luiz", "Maria"]
lista_b = lista_a.copy()

lista_a[0] = "Qualquer coisa"
print(lista_b)