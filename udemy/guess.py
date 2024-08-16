# import random

# secret = random.randint(1, 10)
# guess = int(input("Digite um numero de 0 a 10: "))
# contador = 0


# while guess != secret:
#     if guess > 10:
#         break
#     print("tente novamente")
#     contador += contador
#     if contador >= 10:
#         print("você excedeu o numero de tentativas")
#         break
#     guess = int(input("Digite um número de 1 a 10: "))
# if guess == secret:
#     print("acertou miseravel{True}")



from random import shuffle, randint

# mylist = [1,2,3,4,5,6,7,8,9,0]

# mylist = list(range(0,11))

# print(mylist)

# shuffle(mylist)

# print(mylist)



# ramm = randint(0,100)

# print(ramm)





# mystring = "hello"
# mylist = [letter for letter in mystring]


# # print(mylist)

# celcius = [0,10,20,34.5]

# farenheit = [((9/5)*temp + 32) for tem in celcius]


# celcius = [0,10,20,34.5]

# farenheit = []

# for temp in celcius:
#     farenheit.append(((9/5)*temp + 32))

# print(farenheit)



# #começa com S

# st = " Sam print only the words that start with s in this sentence"

# for word in st.split():
#     # if word.lower().startswith("s"):
#     if word[0].lower() == "s":
#         print(word)

# # Use range() to print all the even numbers from 0 to 10.

# list1 =list(range(0,11,2))
# print(list1)
# for num in range(0,11,2):
#     print(num)



# # # de um a 50 que pode ser divididos por 3
# X = [x for x in range(1,51) if x%3 == 0]
# print(X)


# #Go through the string below and if the lengh of word is even print "even"
# st = "Print every word in this sentence that has an even number of letters"
# for word in st.split():
#     if len(word)%2 ==0:
#         print(f"{word} is even!")



## Escreva um programa que printa os numeros de 1 a 100, mas para os multiples de três print a palavra "fizz"
## no lugar do numero e para os multiples de 5 print a palavra "buzz" para os multiples de 3 e 5 print a palavra fizzbuzz


# for num in range(1,101):
#     if num%3 == 0 and num%5 == 0:
#         # print(f"{num} FizzBuzz")
#         print("FizzBuzz")
#     elif num%3 == 0:
#         # print(f"{num} Fizz")
#         print("Fizz")
#     elif num%5 == 0:
#         # print(f"{num} Buzz")
#         print("Buzz")
#     else:
#         print(num)


# for i in range(1, 22):  # Pode ajustar o range conforme necessário
#     if i % 3 == 0:
#         print(f"{i} pin", end=', ')
#     else:
#         print(i, end=', ')



## st = "Create a list of the first letters of every world in this strings"
# # for i in st.split():
# #     lista = list(i[0])
# #     print(lista, end=",")
# lista = [word[0] for word in st.split()]
# print(lista)







# mylist = [1,2,3]

# mylist.append(4)

# mylist.pop

# help(mylist.insert)


# print(mylist)