n = input('Digite algo: ')

print(f'O tipo primitivo desse valor é {type(n)}')
print(f'So tem espaços {n.isspace()}')
print(f'É um numero ? {n.isnumeric()}')
print(f'É alfabetido ? {n.isalpha()}')
print(f'É alfanumérico ? {n.isalnum()}')
print(f'Esta em maiuscula ? {n.isupper()}')
print(f'Esta em minuscula ? {n.islower()}')
print(f'Esta capitallizada ? {n.istitle()}')