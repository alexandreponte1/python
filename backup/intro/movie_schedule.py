current_movies = {"Matrix":"11:20am",
                  "Hobbit":"3:00pm",
                  "Lord of the Rings":"10:00pm",
                  "House":"2:00pm"}

print("We're sowing the following movies:")
for key,value in current_movies.items():
    print(f"{key} : {value}")


movie = input("What movie would you like the showtime for\n")