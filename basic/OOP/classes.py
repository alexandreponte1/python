employee1 = {
    "name": "John So",
    "age": 38,
    "position": "developer",
    "salary": 1200
}

employee2 = {
    "name": "Lauren",
    "age": 44,
    "position": "tester",
    "salary": 1000  
}


def increase_salary(employee, percent):
    employee["salary"] += employee["salary"] * percent / 100
    # return employee

employees = [employee1, employee2]

for e in employees:
    print(f"{e['name']}'s salary is ${e['salary']}")
