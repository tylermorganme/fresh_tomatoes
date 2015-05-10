import webbrowser


class Movie():
    """This class stores data for movies"""

    def __init__(self, movie_title, movie_storyline, movie_rating, movie_director, poster_image, trailer_youtube_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.rating = movie_rating
        self.director = movie_director
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube_url

    # Opens a web browser and displays the Fresh Tomatoes page
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
