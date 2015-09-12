import webbrowser

class Movie():
    #Constructor
    """This program creates a web page of my favourite movies"""

    VALID_RATINGS=["G","VG","E","O"]
    def __init__ (self,movie_title,movie_storyline,poster_image,trailer):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
