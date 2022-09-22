# loop infinito
# while True:
#     print('lopping')


# count = 1
# while count <= 4:
#     print('lopping')
#     count += 1

# count = 0
# while count < 10:
#     print('lopping')
#     count += 1


count = 0
while count < 10:
    if count % 2 == 0:
        count += 1
        continue
    print(f"where contiung odd number: {count}")
    count += 1