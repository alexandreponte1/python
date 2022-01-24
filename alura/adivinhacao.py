print("********************************")
print("Bem vindo ao Jogo de Advinhação!")
print("********************************")

numero_secreto = 42

chute_str = input("Digite seu Número: ")

print("Você digitou", chute_str)

chute = int(chute_str)

if(numero_secreto == chute):
    print("Você Acertou!")
else:
    print("você errou!")

print("Fim do Jogo")
