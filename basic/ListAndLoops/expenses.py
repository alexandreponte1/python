expenses = [10.50, 8, 5, 15, 20, 5, 3]

# sum = 0

# for x in expenses:
#    sum = sum + x
# print("you spent $", sum, sep = "")


# total = sum(expenses)
# print("you spent $", total, sep = "")


total = 0 
expenses = []

for i in range(7):
   expenses.append(float(input("Enter an expense: ")))

total = sum(expenses)

print("you spent $", total, sep="")