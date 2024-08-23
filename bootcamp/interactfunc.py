from random import shuffle

example = [1,2,3,4,5,6,7]
# shuffle(example)
# print(example)


# result = shuffle_list(example)
# print(result)




# result = shuffle_list(mylist)
# # print(result)




def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


def player_guess():

    guess = ""
    while guess not in ["0","1","2"]:
        guess = input("Pick a number: 1,0 or 2 ")

    return int(guess)


# myindex = player_guess()

# print(myindex)

def check_guess(mylist,guess):
    if mylist[guess] == "O":
        print("Correct!")
    else:
        print("wrong guess!")
        print(mylist)




#Initial list
mylist = [" ", "O", " "]


# shuffle list
mixedup_list = shuffle_list(mylist)


# User Guess
guess = player_guess()

# check guess
result = check_guess(mixedup_list,guess)
print(result)