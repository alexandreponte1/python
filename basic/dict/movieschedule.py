current_movies = {'The Grinch': '11:00am',
                  'Rudolph': '1:00pm',
                  'Frosty The snowan': '3:00am',
                  'Christmas Vaction': '5:00pm'}

print("We're showing the following movies: ")
# print(current_movies)
for key in current_movies:
   print(key)
movie = input('What movie would you like the showtime for?\n ')

showtime = current_movies.get(movie)
if showtime == None:
   print("The Requested movie isn't playing")
else:
   print(movie, 'is playint at', showtime)