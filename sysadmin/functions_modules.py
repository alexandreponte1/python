def hello(name):
    print(f"hi, {name} ")

hello("Ed")
#######

def add (a, b):
    return(a + b)

res = add(1, 2)

print(f"Sum: {res}")
##########


def power (base, exp=2):
    return base ** exp

print ("2ˆ3", power(2,3))
print ("2ˆ3", power(2))


#####

def concatenar(*args):
    r = " "
    for arg in args:
        r +=arg
    return r

print(concatenar("Hi, ", "world"))
print (concatenar("python", " ", "ïs", " ", "amazing" ))