
# Dicionarios

ages = {'kevin': 59, 'alex':29, 'bob':40 }

ages['kayla'] = 22

print(ages)

# evitar
del ages['kevin']

# safe
ages.pop('alex')

ages = {'kevin': 59, 'alex':29, 'bob':40 }

ages.keys()

list(ages.keys())

ages.values()

list(ages.values())


#usar funcao pra criar um dicionario

weights = dict(kevin=80, bob=102, kayla=65)

print(weights)


colors = dict([('kevin', 'blue'), ('bob', 'green'), ('kayla', 'red')])

print(colors)