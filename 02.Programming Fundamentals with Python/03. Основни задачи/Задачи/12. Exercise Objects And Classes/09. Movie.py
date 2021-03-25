# Create a class Movie. The __init__ method should receive a name and director.
# It should also have default value of an attribute watched to be False.
# There should also be a class attribute __watched_movies which will keep
# track of all the watched movies. The class should have the following methods:
# 	change_name(new_name) - changes the name of the movie
# 	change_director(new_director) - changes the director of the movie
# 	watch() - change the watched attribute to True and increase the total
# watched movies class attribute (if the movie is not already watched)
# 	__repr__() - returns "Movie name: {name}; Movie director: {director}. Total watched movies: {__watched_movies}"

class Movie:
	__watched_movies = 0
	def __init__(self, name, director):
		self.director = director
		self.watched = False
		self.name = name

	def change_name(self, new_name):
		self.name = new_name

	def change_director(self, new_director):
		self.director = new_director

	def watch(self):
		if not self.watched:
			Movie.__watched_movies += 1
		self.watched = True

	def __repr__(self):
		return f"Movie name: {self.name}; Movie director: {self.director}. Total watched movies: {Movie.__watched_movies}"


first_movie = Movie("Inception", "Christopher Nolan")
second_movie = Movie("The Matrix", "The Wachowskis")
third_movie = Movie("The Predator", "Shane Black")
forth_movie = Movie("Game of thrones", 'GG Martin')
first_movie.change_director("Me")
third_movie.change_name("My Movie")
first_movie.watch()
third_movie.watch()
first_movie.watch()
forth_movie.watch()
print(first_movie)
print(second_movie)
print(third_movie)
print(forth_movie)

