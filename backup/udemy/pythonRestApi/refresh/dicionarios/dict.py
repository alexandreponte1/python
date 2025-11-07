# friend_ages = {"Rolf": 24, "Jen": 90, "Adam": 78 }
# friend_ages["Rolf"] = 20
# print(friend_ages["Rolf"])
# print(friend_ages)


# friend = [
#     {"Name": "Rolf", "age" : 32},
#     {"Name": "Jen", "age" : 30},
#     {"Name": "Adam", "age" : 78},
# ]


# print(friend[1]["Name"])


######


student_atendent = {"Rolf": 96, "Jen": 80, "Adam": 100 }

# for student, atendent  in student_atendent.items():
#     print(f"{student}:{atendent}")



# if "Rolf" in student_atendent:
#     print(f"Rolf: {student_atendent["Rolf"]}")
# else:
#     print("Rolf is not one of the students")


#get only the values.


attedendence_values = student_atendent.values()
print(sum(attedendence_values) / len(attedendence_values))









