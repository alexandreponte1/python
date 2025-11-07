import requests

link = 'https://minhaapi.alexandreponte.repl.co/pegarvendas'
requisicao = requests.get(link)

print(requisicao)
print(requisicao.json())

dicionario = requisicao.json()

print(dicionario['total_vendas']) 



# https://minhaapi.alexandreponte.repl.co/pegarvendas