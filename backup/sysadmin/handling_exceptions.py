# try:
#     num = int(input("Enter a number: "))
#     r = 10 / num
#     print(f"result: {r}")
# except ZeroDivisionError:
#     print("Error: You cannot divide by zero")
# except ValueError:
#     print("Error: Enter a valid number")
# except Exception as e:
#     print(f"An error occurred: {e}")
# else:
#     print("No exceptions occurred")
# finally:
#     print("execution complete")


# def calculate_age(year_born):
#     current_year = 2023
#     if year_born > current_year:
#         raise ValueError("Invalid birth yaer")
#     return current_year - year_born
    

# try:
#     birth_year = int(input("Enter birth year: "))
#     age = calculate_age(birth_year)
#     print(f"Age: {age}")
# except ValueError as ve:
#     print(f"Error: {ve}")
    
# goku = calculate_age(1985)
# print(f"{goku}")


class InsufficientFundsError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Insufficient funds")
    return balance - amount

try:
    account_balance = 500
    withdraw_amount = int(input("Enter an ammount to withdraw"))
    remaining_balance = withdraw(account_balance, withdraw_amount)
    print(f"Remaining balance: {remaining_balance}")
except InsufficientFundsError as ife:
    print(f"Error: {ife}")