# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

# import copy

# pessoa ={
#     'nome': 'Alexandre',
#     'sobrenome': 'Ponte',
#     # "idade":  900

# }

# pessoa.setdefault("idade", None )
# print(pessoa["idade"])



# print(pessoa.__len__())
# print(len(pessoa))
# print(pessoa.keys())
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))






# for chave in pessoa:
#     print(chave)



# for valor in pessoa.values():
#     print(valor)


# for chave, valor in pessoa.items():
#     print(chave,valor)


# d1 = {
#     "c1" : 1,
#     "c2" : 1,
#     "l1": [0,1,2,3]  #a shalow copy não vai entrar em sublistas apenas a parte rasa
# }

# d2 = d1

# d2["c1"] = 1000

# print(d1)

#fazer com que um dicionario não afete o outro utlizando copy()

# d2 = d1.copy()

# d2 = copy.deepcopy(d1) #afeta 

# d2["c1"] = 1000
# d2["l1"][1]  = 999999

# print(d1)
# print(d2)



#simples copy(), é uma copia rasa, caso queira copiar tudo deve ser feito um deep copy utilizando um import do modulo.




p1 = {
    'nome': 'Alexandre',
    'sobrenome': 'Ponte',
    }

# # print(p1["nome"])
# print(p1.get("nome", "não existe")) #usando get se a chave não existe ele já retorna none

# nomte = p1.pop("nome")
# print(nome)
# print(p1)

# ultimachave = p1.popitem() # remove a ultima chave
# print(ultimachave)
# print(p1)


# p1.update({
#     "nome" : "novo valor",
#     "idade" : 30,
# })

# p1.update(nome="novo valor", idade=9000)

# tupla = ("nome", "novo valor"), ("idade", 80)
lista = [["nome", "novo valor"], ["idade", 80]]

p1.update(lista)
print(p1)