"""Laço for"""

# texto = "Python"


# senha_salva = "123456"
# senha_digitada = ""
# repeticoes = 0

# while senha_salva != senha_digitada:
# #     senha_digitada = input(f"Sua senha ({repeticoes}x): ")
# #     repeticoes += 1

# #     if repeticoes >= 5:
# #         break
# # print(repeticoes)

# # print("Aquele laço acima pode ter infinitas repeticoes")


# texto = "Python"
# novo_texto =""

# for letra in texto:
#     novo_texto += f"*{letra}"

# print(novo_texto)

mylist= [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    newnu = f"*{num}*"
    print(newnu, end="")



mylist= [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    if num % 2 == 0:
        print(num)
    else:
        print("odd number: {}")