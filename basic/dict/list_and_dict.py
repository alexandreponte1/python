# breakfast = ['Pancakes', 'Omelette', 'French Toast']
# lunch = ['Grilled Chicken', 'Pasta', 'Burger']
# dinner = ['Steak', 'Salmon', 'Lasagna']


# menus = [['Pancakes', 'Omelette', 'French Toast'],
#         ['Grilled Chicken', 'Pasta', 'Burger'],
#         ['Steak', 'Salmon', 'Lasagna']]

# print("Breakfast menu:\t", menus[0])
# print("Lunch menu:\t", menus[1])
# print("Dinner menu:\t", menus[2])

# print(menus[0][1])



menus = {'Breakfast' : ['Pancakes', 'Omelette', 'French Toast'],
         'Lunch' : ['Grilled Chicken', 'Pasta', 'Burger'],
         'Dinner' : ['Steak', 'Salmon', 'Lasagna']}

print("Breakfast menu:\t", menus['Breakfast'])
print("Lunch menu:\t", menus['Lunch'])
print("Dinner menu:\t", menus['Dinner'])

# for item in menus:
#    print(item)

print("##################")
for name, menu in menus.items():
   print(name, ":", menu)