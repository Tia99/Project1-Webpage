import jinja2
import webapp2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'name': 'Bill'
        }
        template = JINJA_ENVIRONMENT.get_template('main.html')
        self.response.write(template.render(template_values))

class CommentHandler(webapp2.RequestHandler):
    def post(self):
        user_name = self.request.get("username")
        comment = self.request.get("comment")
        self.redirect("/")

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/comment', CommentHandler)
], debug=True)
