"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# entrada = input('Digite um número: ')
# entrada_int = int(entrada)
# if entrada_int % 2 == 0:
#     print(entrada_int)
# else:
#     print (f'é impar  {entrada_int}')

# entrada = input('Digite um número: ')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'impar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'o numero {entrada_int} é {par_impar_texto}')
# else:
#     print('Você não digitou um número inteiro')



"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# import datetime

# data = datetime.datetime.now()
# hora = data.strftime("%H")

# hora = input('Digite a hora em números inteiros: ')

# try:
#     hora = int(hora)

#     if hora >= 0 and hora <= 11:
#         print('Bom dia')
#     elif hora >= 2 and hora <= 17:
#         print('Boa tarde')
#     elif hora >= 2 and hora <= 17:
#         print('Boa noite')

# except:
#     print('Que burro!!!')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

# nome = input('Digite seu nome: ')

# tamanho_nome = len(nome)

# print(tamanho_nome)

# try:

#     if tamanho_nome >= 1 and tamanho_nome <= 4:
#         print('Seu nome é curto')
#     elif tamanho_nome >= 5 and tamanho_nome <= 6:
#         print('Seu nome é normal')
#     elif tamanho_nome >= 6:
#         print('Seu nome é muito grande')

# except:
#     print('Que burro!!!')

