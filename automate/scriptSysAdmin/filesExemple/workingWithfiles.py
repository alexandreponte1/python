xmen_file = open('xmen_base.txt', 'r')
# print(xmen_file)
# # print(xmen_file.read())

# # print(xmen_file.seek(0))
# print("new_line")
# for line in xmen_file:
#     print(line, end="")

# xmen_file.close

# print (xmen_file.name)

new_xmen = open('new_xmen.txt', 'w')
# print(new_xmen)

new_xmen.write(xmen_file.read())


new_xmen = open(new_xmen.name, 'r+')
# print(new_xmen.read())

print(new_xmen.write("Beast\n"))

print(new_xmen.write("Phoenix\n"))



print(new_xmen.read())
