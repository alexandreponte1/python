import random

computer_choice = random.choice(["rock", "papper", "scissors"])
user_choice = input("Do you want rock, papper or scissors? ")

print ("Computer choice: ", computer_choice)

if computer_choice == user_choice:
   print("TIE")
elif user_choice == "rock" and computer_choice == "scissors":
   print("WIN")
elif user_choice == "papper" and computer_choice == "rock":
   print("WIN")
elif user_choice == "scissors" and computer_choice == "papper":
   print("WIN")
else:
   print("You lose, computer wins :) ")

