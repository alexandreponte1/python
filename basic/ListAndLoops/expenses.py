# expenses = [10.50, 8, 5, 15, 20, 5, 3]

# sum = 0

# for x in expenses:
#    sum = sum + x
# print("you spent $", sum, sep = "")


# total = sum(expenses)
# print("you spent $", total, sep = "")
#range(2, 14, 2) Vai ser assim (2,4,6,8,10,12)
#vai de 2 a 14 com o intervalo de 2 em 2

# total = 0 
# expenses = []

# for i in range(7):
#    expenses.append(float(input("Enter an expense: ")))

# total = sum(expenses)

# print("you spent $", total, sep="")



total = 0 
expenses = []
num_expenses = int(input("Enter # of expenses: "))

for i in range(num_expenses):
   expenses.append(float(input("Enter an expense: ")))

total = sum(expenses)

print("you spent $", total, sep="")