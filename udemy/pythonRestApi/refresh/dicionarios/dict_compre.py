users = [
    (0, "Bob", "password"),
    (0, "Rolf", "bob123"),
    (0, "Jose", "longp4ssword"),
    (0, "username", "1234")

]


username_mapping = {user[1]: user for user in users}
print(username_mapping["Bob"])



# print(users[0][1])