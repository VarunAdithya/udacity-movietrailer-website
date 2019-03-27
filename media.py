import webbrowser

"""This class provides Title,Rating & Duration to Movies and TvShow sub-class"""


class Video():
    """
    This is a parent class that has common inputs for movie & tv shows
    Arguments are Title, Duration, Genre & Rating
    """

    def __init__(self, title, duration, genre, rating):
        self.title = title
        self.duration = duration
        self.genre = genre
        self.rating = rating


class Movie(Video):
    """
    This is a child class named Movie that defines a class movie that is used to display
    information about your favourite Movie Arguments are Titile, Duration, Genre, Rating,
    Poster_Image link & Youtube link
    """

    def __init__(
            self,
            title,
            movie_storyline,
            duration,
            genre,
            rating,
            poster_image,
            trailer_youtube):
        Video.__init__(self, title, duration, genre, rating)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


class TvShow(Video):
    """
    This is a child class named TvShow that defines a class tvshows that is used to display
    information about your favorite TV Shows Arguments are Titile, Duration, Genre, Rating,
    Poster_Image link & Youtube link
    """

    def __init__(
            self,
            title,
            tv_storyline,
            duration,
            genre,
            rating,
            poster_image,
            trailer_youtube):
        Video.__init__(self, title, duration, genre, rating)
        self.storyline = tv_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webrowser.open(self.trailer_youtube_url)
