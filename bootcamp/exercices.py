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



# def makestwenty(n1,n2):
#     return (n1+n2) == 20 or n1==20 or n2==20



# result = makestwenty(10,3)

# print(result)



# LEVEL 1 PROBLEMS
# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

 
# old_macdonald('macdonald') --> MacDonald

# Note: 'macdonald'.capitalize() returns 'Macdonald'

# def old_macdonald(name):
#     ## first_leter = name[0]
#     ## inbetween = name[1:3]
#     ## fourth_letter = name[3]
#     ## rest = name[4:]
#     ## return first_leter.upper() + inbetween + fourth_letter.upper() + rest

#     first_half = name[:3]
#     second_part = name[3:]
#     return first_half.capitalize() + second_part.capitalize()


# name = old_macdonald("macdonald")
# print(name)






# MASTER YODA: Given a sentence, return a sentence with the words reversed

# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'

# Note: The .join() method may be useful here. The .join() method allows you to join together strings in a list with some connector string. For example, some uses of the .join() method:

# >>> "--".join(['a','b','c'])
# >>> 'a--b--c'

# This means if you had a list of words you wanted to turn back into a sentence, you could just join them with a single space string:

# >>> " ".join(['Hello','world'])
# >>> "Hello world"

# def master_yoda(text):
#     wordlist = text.split()
#     reverse_word_list = wordlist[::-1]
#     return " ".join(reverse_word_list)
#     pass

# # Check
# home = master_yoda('I am home')
# print(home)


# # Check
# ready = master_yoda('We are ready')
# print(ready)






# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True

## #NOTE: abs(num) returns the absolute value of a number

# def almost_there(n):
#     return (abs(100-n)<=10) or (abs(200-n)<=10)

#     pass

# # Check
# print (almost_there(104))

# # Check
# print(almost_there(150))

# # Check
# print(almost_there(209))




# LEVEL 2 PROBLEMS
# FIND 33:

# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

# def has_33(nums):
#     for i in range(0,len(nums)-1):
#         if nums[i:i+2] == [3,3]:
#         # if nums[i] == 3 and nums[i+1] == 3:
#             return True
#     return False

# # Check
# print (has_33([1, 3, 3]))

# # Check
# print(has_33([1, 3, 1, 3]))

# # Check
# print(has_33([3, 1, 3]))




# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

# def paper_doll(text):
#     result = ""
#     for char in text:
#         result += char*3
#     return result

# # Check
# print(paper_doll('Hello'))


# # Check
# print(paper_doll('Mississippi'))




# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19

# def blackjack(a,b,c):
#     if sum([a,b,c]) <= 21:
#         return sum([a,b,c])
#     elif 11 in [a,b,c] and sum([a,b,c]) <= 31:
#         return sum([a,b,c]) -10
#     else: 
#         return "BUST"

# # Check
# print(blackjack(5,6,7))

# # Check
# print(blackjack(9,9,9))

# # Check
# print(blackjack(9,9,11))





# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14

def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num!= 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num!= 9:
                break
            else:
                add = True
    return total


# Check
print(summer_69([1, 3, 5]))

# Check
print(summer_69([4, 5, 6, 7, 8, 9]))

# Check
print(summer_69([2, 1, 6, 9, 11]))

