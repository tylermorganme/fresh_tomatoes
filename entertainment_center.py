import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A movie about toys coming to life",
                        "G",
                        "John Lasseter",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc");

princess_mononoke = media.Movie("Princess Mononoke",
                                "A young man and a feral woman must save the world.",
                                "PG-13",
                                "Hayao Miyazaki",
                                "http://ia.media-imdb.com/images/M/MV5BMjgzNTUwODQzN15BMl5BanBnXkFtZTcwMTc4ODE3OQ@@._V1_SX214_AL_.jpg",
                                "https://www.youtube.com/watch?v=4OiMOHRDs14")

con_air = media.Movie("Con Air",
                     "After a violent highjacking, a convict must help the police.",
                     "R",
                     "Simon West",
                     "http://ia.media-imdb.com/images/M/MV5BMTU1NzY2NjIzNV5BMl5BanBnXkFtZTgwMzE2Mzk5MDE@._V1_SY317_CR0,0,214,317_AL_.jpg",
                     "https://www.youtube.com/watch?v=fWq-S1_1vnc")

shawshank_redemption = media.Movie("The Shawshank Redemtion",
                                   "Life in prison isn't all it's cracked up to be.",
                                   "R",
                                   "Frank Darabont",
                                   "http://ia.media-imdb.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_SX214_AL_.jpg",
                                   "https://www.youtube.com/watch?v=6hB3S9bIaco");

# Contains all instances of Movie that will be displayed on the page
movies = [toy_story, princess_mononoke, con_air, shawshank_redemption]

fresh_tomatoes.open_movies_page(movies)
