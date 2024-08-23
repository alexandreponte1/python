# stock_prices = [("APPL",200),("GOOGLE",400),("MSFT",100)]


# for item in stock_prices:
#     print(item)

# for ticker,price in stock_prices:
#     print(ticker)




# for ticker,price in stock_prices:
#     print(price+(0.1*price))



work_hours = [("Alexandre",1000),("Billy", 4000),("Cassie",800)]


def employee_check(work_hors):
    current_max = 0
    employee_of_mounth = ""

    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_mounth = employee
        else:
            pass

    return (employee_of_mounth, current_max)



# result = employee_check(work_hours)

# print(result)


# name,hours,location = employee_check(work_hours)

# print(name)

item = employee_check(work_hours)

print(item[0])

