import sys

A = input("Digite o primeiro valor: ")
B = input("Digite o segundo valor: ")

try:
    A_float = float(A)
    B_float = float(B)
except ValueError:
    print("um dos valores não é inteiro.")
    sys.exit()

print("Ambos os valores são inteiros.")

funcao = input("escolha uma funcao (soma, subtracao): ")

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

if funcao == "soma":
    resultado = soma(A_float, B_float)
    print("resultado da soma é:", resultado)
elif funcao == "subtracao":
    resultado = subtracao(A_float, B_float)
    print("resultado da subtracao é:", resultado)
else:
    print("funcao invalida.")
    