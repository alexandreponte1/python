def add(x,y):
    return x + y


print(add(5,6))

add = lambda x,y: x + y


print(add(5,8))



def double(x):
    return x * 2


sequence = [1,3,5,9]
doubled = [x * 2 for x in sequence]
doubled = [double(x) for x in sequence]
doubled = list(map(double, sequence))

doubled = list(map(lambda x: x * 2, sequence))



print(doubled)