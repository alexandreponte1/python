# nomes = ["Maria", "Alex", "Luiz",]
# nome1, nome2, nome3 = nomes

nome1, nome2, nome3 = ["Maria", "Alex", "Luiz",]
# nome1, nome2 = ["Maria", "Alex", "Luiz",]
# nome1, nome2, nome3, nome4 = ["Maria", "Alex", "Luiz",]

# nome1, *resto = ["Maria", "Alex", "Luiz",]



# print(nome1, resto)

_, nome, *resto = ["Maria", "Alex", "Luiz",]



print(nome, resto)