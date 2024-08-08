
# if
age = 18
if age >= 18:
    print("You are now an adult:")

temp = 25
if temp > 30:
    print("ta quente lá fora")
else:
    print("ta de boa")

res = 70
if res >= 90:
    grade = "A"
elif res >= 80:
    grade = "B"
elif res >= 70:
    grade = "C"
else:
    grade = "D"
print(f"your grade obtained is {grade}")


##FOR LOPP

fruits = ["maça", "banana", "uva"]
for fruit in fruits:
    print(f"fruta atual: {fruit}")

for num in range(1, 6):
    print(f"Number: {num}")


numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num % 2 ==0:
        print(f"skipping this event number: {num}")
        continue
    print(f"Current number: {num}")


for i in range (3):
    for j in range(3):
        print(f"i: {i} j: {j}")


def recursive(i, j):
    if i < 3:
        if j < 3:
            print(f"i: {i} j: {j}")
            recursive(i, j + 1)
        else:
            recursive(i + 1, 0 )
    else:
        return
recursive(0, 0)

#WHILE LOOP
cnt = 0
while cnt < 5:
    print(f"Cont: {cnt}")
    cnt += 1

