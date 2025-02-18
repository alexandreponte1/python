age = 18
if age >= 18:
    print("You are now an adult")

temp = 25
if temp > 30:
    print("its warn outside")
else:
    print("its not too hot")


res = 85 
if res >= 90:
    grade = "A"
elif res >= 80:
    grade = "B"
elif res >= 70:
    grade = "C"
else:
    grade = "D"

print(f"Your grade obtained is {grade}")

fruits = ["apple", "banana", "grape"]

for fruit in fruits:
    print(f"Current fruit: {fruit}")

print(fruits[0])