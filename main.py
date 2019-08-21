import webapp2
import jinja2
import os

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.qutoscape'],
    autoescape=True)


class Username(webapp2.RequestHandler):
    def get(self):
        resultstemplate = the_jinja_env.get_template('templates/index.html')
        self.response.write(results_template.render())

class Character(webapp2.RequestHandler):



    app = webapp2.WSGIApplication([
        ('/Name', Username),
        ('/Character', Character)
        ], debug=True)
