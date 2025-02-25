# 11-8. Movie List

movies = []

def add_movie(movie_list, movie):
  movie_list.append(movie)

def remove_movie(movie_list, movie):
  # reason we need this check is because .remove() raises an Error if the movie isn't in the list.
  if movie in movie_list:
    movie_list.remove(movie)

def print_movie_list(movie_list):
  # print(movie_list) is perfectly fine but let's loop through it for extra practice!
  for movie in movie_list:
    print(movie)

add_movie(movies, "Ratatouille")
add_movie(movies, "Mulan")
add_movie(movies, "WALL-E")

remove_movie(movies, "WALL-E")
remove_movie(movies, "Cinderella") # won't do anything since Cinderella isn't in our list.

print_movie_list(movies)