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

    def post(self):
        username_entered = self.request.get('username')
        comment_entered = self.request.get('comment')
        if self.valid_username(username_entered) and self.valid_comment(comment_entered):
            #TODO: save to db
            self.redirect('/')
        else:
            template_values = {
                'error': 'Username or comment are not valid!',
                'username': username_entered,
                'comment': comment_entered
            }
            template = JINJA_ENVIRONMENT.get_template('main.html')
            self.response.write(template.render(template_values))

    def valid_username(self, s):
        m = len(s)
        if m > 1 and m < 15:
            return True
        else:
            return False

    def valid_comment(self, s):
        m = len(s)
        if m > 5 and m < 1000:
            return True
        else:
            return False




app = webapp2.WSGIApplication([
    ('/', MainPage),    
], debug=True)
