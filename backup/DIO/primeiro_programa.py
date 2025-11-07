print ("Olá Mundo!")
print(1 + 10)
print(1.5 + 0.5 )
print(True, False)

int()
##############################################################################################################
#variaveis constates não existem em python, mas por convenção ela é declarada com maiuscula
# ex:

DEBUG = True

STATES = [
    'SP',
    'MG',
    'RJ'
]
AMOUNT = 30.2

##############################################################################################################

#Padrão de nomes é SNAKE CASE
#EX:
preco_total = 100


nome = "Alexandre"
idade = "41"


nome, idade = "goku", "50"


print(nome, idade)
limite_saque_diario = 1000
print(limite_saque_diario)

BRAZILIAN_STATES = [
    'SP',
    'MG',
    'RJ'
]
print(BRAZILIAN_STATES)


idade = int(25)

preco = 2.0

texto  = f"idade {idade} preco {preco}"

print(texto)


print(5 // 2)
    

#if ternario
saldo = 2000
saque = 2500

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque")


# estrutura for

texto = input("informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=",")
print() #adiciona uma quebra de linha 

#range

for numero in range(0,10):
    print(numero, end="")
print()

# for numero in range(10):
#     print(numero, end="")
# print
# range inicio, fim e step
for numero in range(5, 51, 5):
    print(numero, end=" ")
print()