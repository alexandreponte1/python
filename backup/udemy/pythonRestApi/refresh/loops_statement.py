

number = 7 
while True:
    user_input = input(" you would like to play (y/n)")
    if user_input == "n":
        break
    user_number = int(input("Enter your guess: "))
    if user_number == number:
        print("you guess right")
    elif abs(number - user_number) == 1:
        print("you where of by one")
    else:
        print("wrong guess")