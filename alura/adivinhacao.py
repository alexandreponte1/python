print("********************************")
print("Bem vindo ao Jogo de Advinhação!")
print("********************************")

numero_secreto = 42

total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
##Interpolação de String##
    print("Tentativa {} de {} ".format(rodada, total_de_tentativas))
    chute_str = input("Digite seu Número: ")
    print("Você digitou", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print("Você Acertou!")
    else:
        if(maior):
            print("você errou! O seu chute foi maior do que o numero secreto.")
        elif(menor):
            print("você errou! O seu chute foi menor do que o numero secreto.")

    rodada = rodada + 1

print("Fim do Jogo")
