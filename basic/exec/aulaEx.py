# # idade = 4
# # print(idade)


# altura = 1.75
# print(altura)

# curso = "python"
# print("Estou aprendendo " + curso)

# nome = input("Digite seu nome: ")
# print("Olá", nome, "! Seja bem vindo!")

# boleano = False
# print(boleano)

# idade = 35
# print("Minha idade é ", idade)


# ano_de_nascimento = int(input("Digite o ano do seu nascimento: "))
# ano_atual = 2025
# idade = ano_atual - ano_de_nascimento
# print("sua idade é ", idade)

# a = 3.5
# b = 2.1
# soma = a / b
# print(soma)


# curso = " uma nova linguagem"
# print("Estou aprendendo " + curso)

# texto = "Ola, mundo"
# texto += " - python"
# print(texto)

# a = True
# b = False
# x = 10 
# y = 5
# resultado = x >= y
# print(resultado)


# nota = float(input("Digite a nota do aluno de (0 a 10): "))


# lista_numeros = [10, 20, 30, 40,50]
# soma = 0
# for numero in lista_numeros:
#    soma += numero
# media = soma / len(lista_numeros)
# print(f"A media dos numeros: {media}")

# lista_de_compras = ["Maças", "Bananas", "Leite", "Pão", "Ovos"]
# print(lista_de_compras)
# for item in lista_de_compras:
#    print("- ", item )

# lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lista_pares = [numero for numero in lista_numeros if numero % 2 == 0] #!=
# print(f"lista de numeros pares, {lista_pares}")




# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# a = [2, 3, 4, 5]
# b = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


# n = int(input().strip()) 

# if n % 2 ==0 and n in a:
#     print("Not weird")
# elif n % 2 == 0 and n in b:
#     print("Weird")
# elif n % 2 == 0 and n > 20:
#     print("Not Weird")
# elif n % 2 != 0:
#     print("Weird")

    
# a = int(input().strip()) 
# b = int(input().strip()) 

# soma = a + b 
# sub = a - b 
# vs = a * b

# print(soma)
# print(sub)
# print(vs)




# if __name__ == '__main__':
#     n = int(input())
#     for i in range(n):
#         print(i * i)

# a = []

# if __name__ == '__main__':
#     n = int(input())
#     for i in range(n):
#         a.append(i + 1)
#     print("".join(str(num) for num in a))



# def contar_ocorrencias(palavras):
#    ocorrencia = {}
#    for palavra in palavras:
#       if palavra in ocorrencia:
#          ocorrencia[palavra] += 1
#       else:
#          ocorrencia[palavra] = 1
#    return ocorrencia

# lista_palavras = ["maça", "banana", "maça", "laranja", "banana", "uva"]
# resultado_ocorrencias = contar_ocorrencias(lista_palavras)
# print("Ocorrencia de cada palavra:", resultado_ocorrencias)

# def calcular_soma_media(numeros):
#    soma = sum(numeros)
#    media = soma / len(numeros)
#    return soma, media

# lista_numeros = [10, 20, 30, 40, 50]
# soma_resultado, media_resultado = calcular_soma_media(lista_numeros)
# print(f"soma: {soma_resultado}, Média: {media_resultado}")


#Dicionario de compras
# lista_de_compras = {}
# while True:
#    item = input("Digite um item(Ou 'sair' pra encerrar): ")
#    if item.lower() == 'sair':
#       break
#    quantidade = int(input("Digite a quantidade: "))
#    lista_de_compras[item] = quantidade
# print("Lista de Compras:")
# for item, quantidade in lista_de_compras.items():
#    print(f"{quantidade} {item}")



# WBS = 730X86

import random
numero_secreto = random.randint(1, 10)
tentativas = 0
while True:
   palpite = int(input("Tente advinhar o numero secreto (1-10): "))
   tentativas += 1
   if palpite == numero_secreto:
      print(f"Parabens! Voce Acertou em {tentativas} tentativas.")
      break
   elif palpite < numero_secreto:
      print("Tente um numero maior.")
   else:
      print("tente um numero menor.")


