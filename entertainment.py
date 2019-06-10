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

# Create Despicalbe me 3 trialer
ME3 = movie.Movie(movie_title = "Despicalbe Me 3", movie_storyline = "The mischievous Minions hope that Gru will return to a life of crime after the new boss of the Anti-Villain League fires him. Instead, Gru decides to remain retired and travel to Freedonia to meet his long-lost twin brother for the first time. The reunited siblings soon find themselves in an uneasy alliance to take down the elusive Balthazar Bratt, a former 1980s child star who seeks revenge against the world.", 
poster_image = "https://movies.universalpictures.com/media/dm3-adv1sheet-rgb-5-58c818a68f809-1.png", trailer_youtube = "https://www.youtube.com/watch?v=6DBi41reeF0")

# Create Minion trailer
MINIONS = movie.Movie(movie_title = "Minions", movie_storyline = "Evolving from single-celled yellow organisms at the dawn of time, Minions live to serve, but find themselves working for a continual series of unsuccessful masters, from T. Rex to Napoleon. Without a master to grovel for, the Minions fall into a deep depression. But one minion, Kevin, has a plan; accompanied by his pals Stuart and Bob, Kevin sets forth to find a new evil boss for his brethren to follow. Their search leads them to Scarlet Overkill, the world's first-ever super-villainess.", 
poster_image = "https://m.media-amazon.com/images/M/MV5BMTg2MTMyMzU0M15BMl5BanBnXkFtZTgwOTU3ODk4NTE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
trailer_youtube = "https://www.youtube.com/watch?v=eisKxhjBnZ0")

movies = [ME, ME2, ME3, MINIONS]
website.open_movies_page(movies)