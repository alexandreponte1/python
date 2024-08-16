# def soma(*args): #args é uma convenção poderia ser qualquer coisa seguida do *
#     total = 0
#     for numero in args:
#         total = numero * numero
#     return total




# soma_4_5_6 = soma(3, 3)

# print(soma_4_5_6)

# def impar(x):
#     if x % 2 == 0:
#         print(F"{x} é  numero é par")
#     else:
#         print(F"{x} é  numero é impar")


# impar(soma_4_5_6)

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


multiplicacao = multiplicar(10, 2, 3, 4, 5)
print(multiplicacao)

print(10*2*3*4*5)



def par_impar(numero):
   multiplo_de_dois =  numero % 2 == 0
   if multiplo_de_dois:
       return f"{numero} é par"
   return f"{numero} é Ímpar"




print(par_impar(2))
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))

