from time import localtime, mktime, strftime

start_time = localtime()

print(f"Timer started at {strftime('%X', start_time)}")

# wait for user to stop timer
input ("Press 'ENTER' to stop timer")


stop_time = localtime()
difference = mktime(stop_time) - mktime(start_time)

print(f"Timer stopped at {strftime('%X', stop_time)}")

print(f"total time:{difference} seconds")






