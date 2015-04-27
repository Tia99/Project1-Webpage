import webbrowser
class Movie():
    def __init__(self, movie_title, trailer_youtube):
        self.title = movie_title
        self.trailer = trailer_youtube
    def show_trailer(self):
        webbrowser.open(self.trailer)
