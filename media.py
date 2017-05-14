import webbrowser

# Class is a blueprint and can have data and methods
class Movie:
    """This class provides a way to store movie related information"""
    # Class Variable, constants are all CAPS
    # All classes come with predefined Class variables

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    # Constructor of the Class Movie, we initialize and construct all of the data uses
    # key word self
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        # Instance Variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    # instance methods
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
