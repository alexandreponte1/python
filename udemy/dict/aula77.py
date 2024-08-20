#Manipulando chaves e valores em dicionarios

# pessoa ={
#     'nome': 'Alexandre',
#     'sobrenome': 'Ponte',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }


pessoa ={}

pessoa["nome"] = "Alexandre"
pessoa["sobrenome"] = "Ponte"

print(pessoa)
print(pessoa["nome"][0])



del pessoa["sobrenome"]

print(pessoa)


if pessoa.get("sobrenome") is None:
    print("EXISTE")