import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        name = "John"
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<html><head><title>World</title></head><body><h1>Hello '+ name +'!</h1></body></html>')

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
