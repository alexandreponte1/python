# def add(x,y):
#     result = x + y
#     print(result)

# add(5,3)

#################################################################################

# def say_hello(name):
#     print(f"hello, {name}")


# say_hello("goku")


#################################################################################



# def say_hello(name,  surname):
#     print(f"hello, {name} {surname}")



# def say_hello(name="goku",  surname="kakaroto"):
#     pass


# say_hello()

#################################################################################


def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    # else:
    return"you foll! "


result  = divide(15, 0)

print(result)


a = 10
def my_function(param_1=a):
    print(param_1)
a = 20
my_function()