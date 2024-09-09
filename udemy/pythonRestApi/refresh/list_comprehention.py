# numbers = [1,3,5]
# dubled = []


# for number in numbers:
#     dubled.append(number * 2)

# print(dubled)



# dubled = [x * 2 for x in numbers]


#####################

friends = ["Bob", "Rolf", "Anne", "Sam", "Jen","Saruman"]

starts_s = [friend for friend in friends if friend.startswith("S")]

# for friend in friends:
#     if friend.startswith("S"):
#         starts_s.append(friend)

print(starts_s)