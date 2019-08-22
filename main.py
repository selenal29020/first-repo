import webapp2
import jinja2
import os

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def memeStringToUrl(inputCharacter):
    imgUrl = ""
    if inputCharacter == "Male":
        imgUrl = "https://cdn3.iconfinder.com/data/icons/avatars-add-on-pack-1/48/v-06-512.png"
    elif inputCharacter == "Female":
        imgUrl = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcStCfPsQRIgFua7Qa47pdCKS_qvTLHTODOpbVzQv6mt00Qx0VSW"
    return imgUrl

class Username(webapp2.RequestHandler):
    def get(self):
        results_template = the_jinja_env.get_template('Templates/index.html')
        self.response.write(results_template.render())

class Character(webapp2.RequestHandler):
    def get(self):
        results_template = the_jinja_env.get_template('Templates/character.html')
        self.response.write(results_template.render())
    def post(self):
        theFirstLine = self.request.get("user_first_ln")
        print("Received: %s" % (theFirstLine))
        userChar = self.request.get("uname")
        userGen = self.request.get("character_choice")
        var_dict = {
            "user_char": userChar,
            "user_gen": userGen
        }
        results_template = the_jinja_env.get_template('Templates/character.html')
        self.response.write(results_template.render(var_dict))

class StartGameHandler(webapp2.RequestHandler):
    def get(self):
        results_template = the_jinja_env.get_template('Templates/start.html')
        self.response.write(results_template.render())
    def post(self):
        results_template = the_jinja_env.get_template('Templates/start.html')
        theFirstLine = self.request.get("user_first_ln")
        userChar = self.request.get("character_choice")
        var_dict = {
            "line1": theFirstLine,
            "char_img_url": memeStringToUrl(userChar)
        }
        self.response.write(results_template.render(var_dict))

class LevelOneHandler(webapp2.RequestHandler):
    def get(self):
        results_template = the_jinja_env.get_template('Templates/LevelOne.html')
        self.response.write(results_template.render())
    def post(self):
        results_template = the_jinja_env.get_template('Templates/LevelOne.html')
        theFirstLine = self.request.get("user_first_ln")
        userChar = self.request.get("character_choice")
        var_dict = {
            "line1": theFirstLine,
            "char_img_url": memeStringToUrl(userChar)
        }
        self.response.write(results_template.render(var_dict))

class LevelTwoHandler(webapp2.RequestHandler):
    def get(self):
        results_template = the_jinja_env.get_template('Templates/LevelTwo.html')
        self.response.write(results_template.render())
    def post(self):
        results_template = the_jinja_env.get_template('Templates/LevelTwo.html')
        theFirstLine = self.request.get("user_first_ln")
        userChar = self.request.get("character_choice")
        var_dict = {
            "line1": theFirstLine,
            "char_img_url": memeStringToUrl(userChar)
        }
        self.response.write(results_template.render(var_dict))


class DeathHandler(webapp2.RequestHandler):
    def get(self):
        results_template = the_jinja_env.get_template('Templates/Death.html')
        self.response.write(results_template.render())
    def post(self):
        results_template = the_jinja_env.get_template('Templates/Death.html')
        theFirstLine = self.request.get("user_first_ln")
        userChar = self.request.get("character_choice")
        var_dict = {
            "line1": theFirstLine,
            "char_img_url": memeStringToUrl(userChar)
        }
        self.response.write(results_template.render(var_dict))

class HouseHandler(webapp2.RequestHandler):
    def get(self):
        results_template = the_jinja_env.get_template('Templates/House.html')
        self.response.write(results_template.render())
    def post(self):
        results_template = the_jinja_env.get_template('Templates/House.html')
        theFirstLine = self.request.get("user_first_ln")
        userChar = self.request.get("character_choice")
        var_dict = {
            "line1": theFirstLine,
            "char_img_url": memeStringToUrl(userChar)
        }
        self.response.write(results_template.render(var_dict))


class CaveHandler(webapp2.RequestHandler):
    def get(self):
        results_template = the_jinja_env.get_template('Templates/Cave.html')
        self.response.write(results_template.render())
    def post(self):
        results_template = the_jinja_env.get_template('Templates/Cave.html')
        theFirstLine = self.request.get("user_first_ln")
        userChar = self.request.get("character_choice")
        var_dict = {
            "line1": theFirstLine,
            "char_img_url": memeStringToUrl(userChar)
        }
        self.response.write(results_template.render(var_dict))

app = webapp2.WSGIApplication([
    ('/', Username),
    ('/character', Character),
    ('/start', StartGameHandler),
    ('/LevelOne', LevelOneHandler),
    ('/LevelTwo', LevelTwoHandler),
    ('/Death', DeathHandler),
    ('/House', HouseHandler),
    ('/Cave', CaveHandler),
], debug=True)
