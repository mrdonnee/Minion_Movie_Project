# This is the file to call class function
import movie   # import the class defination file name
import website

# Create 1 movie trailer as despicable me
ME = movie.Movie(movie_title = "Despicalbe ME", movie_storyline = "When a criminal mastermind uses a trio of orphan girls as pawns for a grand scheme, he finds their love is profoundly changing him for the better."
, poster_image = "https://m.media-amazon.com/images/M/MV5BYzE3YzIxZjMtY2U1Yy00ZmQwLTgyMjYtZmY5NDhjODg4NDYyXkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_SY1000_SX584_AL_.jpg",
trailer_youtube = "https://www.youtube.com/watch?v=6L2zy5itMGs")  
 # use movie file to do class Movie() function


# Create another movie trailer as despicable me2
ME2 = movie.Movie("Despicalbe ME 2", "When Gru, the world's most super-bad turned super-dad has been recruited by a team of officials to stop lethal muscle and a host of Gru's own, He has to fight back with new gadgetry, cars, and more minion madness.",
"https://m.media-amazon.com/images/M/MV5BMjExNjAyNTcyMF5BMl5BanBnXkFtZTgwODQzMjQ3MDE@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
"https://www.youtube.com/watch?v=-kYzHmPDZwo")



movies = [ME, ME2]
website.open_movies_page(movies)