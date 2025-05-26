# # Get details of loan
# money_owed = float(input("How much money do you owe, in dollar \n")) # $50,000
# apr = float(input("What is the annual percentage rate of the loan \n")) # %3
# payment = float(input("How much will you pay off each month in dollars?  \n")) # $1,000
# months = int(input("How many months do you want to see the results for?   \n")) #24

# monthly_rate = apr/100/12

# for i in range(months):
#    # calculate interest to pay
#    interest_paid = money_owed*monthly_rate

#    # Add in interest
#    money_owed = money_owed + interest_paid

#    if (money_owed - payment < 0 ):
#       print("The last payment is ", money_owed)
#       print("You paid off the loan in", i+1, "months")
#       break

#    # Make payment
#    money_owed = money_owed - payment

#    print("Paid", payment , "of which", interest_paid , "was interest", end=" ")
#    print("Now I owe", money_owed)


# Get details of loan
money_owed = float(input("How much money do you owe, in dollar \n")) # $50,000
apr = float(input("What is the annual percentage rate of the loan \n")) # %3
payment = float(input("How much will you pay off each month in dollars?  \n")) # $1,000
months = int(input("How many months do you want to see the results for?   \n")) #24

monthly_rate = apr / 100 / 12

for i in range(months):
   # calculate interest to pay
   interest_paid = money_owed * monthly_rate

   # Add in interest
   money_owed += interest_paid

   if money_owed - payment < 0:
      print(f"The last payment is ${money_owed:.2f}")
      print(f"You paid off the loan in {i+1} months")
      break

   # Make payment
   money_owed -= payment

   print(f"Paid ${payment:.2f}, of which ${interest_paid:.2f} was interest. Now I owe ${money_owed:.2f}")
