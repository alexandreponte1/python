# days_of_week = input("whats day of the week it is today? ").lower()
# # print(days_of_week == "monday")

# if days_of_week == "monday":
#     print("have a great start to your week!")
# elif days_of_week == "Tuesday":
#     print("its Tuesday")
# else:
#     print("Full speed ahead")

# print("this always run. ")



# movies_watched = {"Matrix", "Seven", "Her"}
# user_movie = input("Enter something you have watched recently: ")

# if user_movie in movies_watched:
#     print(f"I've watched {user_movie} too! ")
# else:
#     print(f"I haven't {user_movie} watched that yet")



number = 7 
user_input = input("enter 'y' if you would like to play: ").lower()

if user_input == "y":
    user_guess = int(input("Enter your guess: "))
    if user_guess == number:
        print("you guess right")
    elif abs(number - user_guess) == 1:
        print("you where of by one")
    else:
        print("wrong guess")

