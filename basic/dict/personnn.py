person = {'name':'Sara Smith',
          'city':'Orlando',
          'age':100}

# print(person['age'])

print(person.get('name'), 'is', person.get('age'), 'Years old.' )

for x in person.items():
   print(x)