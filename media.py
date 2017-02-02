import webbrowser

# Generic video instance variables for movies or TV shows.
class Video():
    def __init__(self, title, duration, storyline, poster_image):
        self.title = title
        self.duration = duration
        self.storyline = storyline
        self.poster_image_url = poster_image

# Movie inherits from Video and contains additional instance variables plus
# show_trailer instance method.
class Movie(Video):
    def __init__(self, title, duration, storyline, poster_image, year,
                 trailer_youtube):
         Video.__init__(self, title, duration, storyline, poster_image)
         self.year = year
         self.trailer_youtube_url = trailer_youtube
     
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)