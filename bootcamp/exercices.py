# def myfunc(x,y,z):
#     if z == True:
#         return x
#     else:
#             z == False
#             return y

# result = myfunc("Hello", "Goodbye", False)

# print(result)






# def myfunc(*args):
#     mylist = []
#     for num in args:
#           if num%2==0:
#                mylist.append(num)
#     return mylist


# result = myfunc(1,2,3,4,5,6)

# print(result)


# def myfunc(*args):
#     out = []
#     for num in args:
#         if num%2==0:
#             out.append(num)
#     return out



# result = myfunc(1,2,3,4,5,6)

# print(result)





# def myfunc(x):
#     out = []
#     for i in range(len(x)):
#         if i%2==0:
#             out.append(x[i].lower())
#         else:
#             out.append(x[i].upper())
#     return ''.join(out)



# def myfunc(x):
#     out = []
#     for i in range(len(x)):
#         if i%2==0:
#             out.append(x[i].lower())
#         else:
#             out.append(x[i].upper())
#     return ''.join(out)







# if len("aa")%2==0:s
#     print(True)


# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd

# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5




# def lesser_of_two_evens(a,b):
#     if a%2 == 0 and b%2 == 0:
#        return  min(a,b)
#     else:
#        return  max(a,b)


# result = lesser_of_two_evens(2,6)
# print(result)



# result = lesser_of_two_evens(11,33)
# print(result)

#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False



# def animal_crackers(a,b):
#     if a[0] == b[0]:
#         return True
#     return False
# result = animal_crackers("Levelheaded", "lama")

# print(result)


#certo
# def animal_crackers(text):
#     wordlist = text.lower().split()
#     return wordlist[0][0] == wordlist[1][0]



# result = animal_crackers('Levelheaded llama')
# print(result)







#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False



def makestwenty(n1,n2):
    return (n1+n2) == 20 or n1==20 or n2==20



result = makestwenty(10,3)

print(result)



# LEVEL 1 PROBLEMS
# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

 
# old_macdonald('macdonald') --> MacDonald

# Note: 'macdonald'.capitalize() returns 'Macdonald'

def old_macdonald(name):
    pass

