# result = 2 % 2

# print(result)


# def even_number(num1,num2):
#     if num1 % num2 == 0:
#         return "even"
#     else:
#         return "not even"
    

# iseven = even_number(2,2)

# print(iseven)

# def even_check(number):
#     return number % 2 == 0


# result = even_check(56356536450)
# print(result)



#Return true if any number is even inside a list



# mylist = [2,4,4,6,1]


# for num in mylist:
#     if num % 2 == 0:
#         print(True)
#     else:
#         print(False)


def check_even_list(num_list):
    #Return all the even numbers in a list
    even_numbers = []
    for number in num_list:
        if number % 2 ==0:
            even_numbers.append(number)
        else:
            pass

    return even_numbers



result = check_even_list([1,2,3,4,5])
print(result)