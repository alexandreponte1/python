
# def myfunc(a,b):
#     # Return 5% of the sun of a and b
#     return sum((a,b)) * 0.05

# result = myfunc(40,60)

# print(result)


# *ARGS
#*args retorna uma tupla
# por convercão usa *args, mas pode se usar outras coisas como *spam

# def myfunc(*args):
#     # Return 5% of the sun of a and b
#     print(*args) # é uma tupla
#     return sum((args)) * 0.05

# result = myfunc(40,60,70,30,44,33,22)

# print(result)






# def myfunc(*args):
#     for item in args:
#         print(item)

# result = myfunc(40,60,70,30,44,33,22)

# print(result)




# **Kwargs
# **kwargs retorna um dicionario


def myfunc(**kwargs):
    print(kwargs)
    if "fruit" in kwargs:
        print("My fruit of choice is {}".format(kwargs["fruit"]))
    else:
        print("I didi not find any fruit here")



myfunc(fruit="apple", veggie="lettuce")

# print(result)




def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)

    print("I would like {} {}".format(args[0],kwargs["food"]))



myfunc(10,20,30,fruit="Orange", food="egg", animal="Dog")
