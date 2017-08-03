#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
from google.appengine.ext import ndb
import os
from google.appengine.api import users
global name

import string


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class MainHandler(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()
        login_url = users.create_login_url('/home')
        logout_url = users.create_logout_url('/home')
        if user:
            nickname = user.nickname()
            greeting = 'Welcome, {}! (<a href="{}">sign out</a>)'.format(
                nickname, logout_url)
        else:
            greeting = '<a href="%s">Sign in</a>' % (login_url)

        my_template = jinja_environment.get_template("templates/home.html")

        self.response.write(my_template.render())



class HangmanHandler(webapp2.RequestHandler):
    def get(self):
        render_dict = {
        "letters": string.ascii_uppercase
        }
        my_template = jinja_environment.get_template("templates/hangman.html")
        self.response.write(my_template.render(render_dict))

class HighScoreHandler(webapp2.RequestHandler):
    def writetemplate(self):
        my_template = jinja_environment.get_template("templates/highscore.html")
<<<<<<< HEAD
        getting_all_results = HighScoreModel.query().fetch()
=======
        username = self.request.get("name")
        userscore =int(self.request.get("gamescore"))
        my_usernames = HighScoreModel(username = username, score= userscore)
        my_usernames.put()
        getting_all_results = HighScoreModel.query().order(-HighScoreModel.score).fetch()
>>>>>>> 293632ade58d3eedca741b4908d753acd70b62ef
        render_data = {
            'users' : getting_all_results
        }
        self.response.write(my_template.render(render_data))
    def get(self):
        self.writetemplate()
    # @ndb.transactional(xg=True)
    def post(self):
        username = self.request.get("name")
        userscore =int(self.request.get("gamescore"))
        my_usernames = HighScoreModel(username = username, score= userscore)
        my_usernames.put()
        self.writetemplate()

class AboutUsHandler(webapp2.RequestHandler):
    def get(self):
        my_template = jinja_environment.get_template("templates/aboutus.html")
        self.response.write(my_template.render())


class SignHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            nickname = user.nickname()
            logout_url = users.create_logout_url('/home')
            greeting = 'Welcome, {}! (<a href="{}">sign out</a>)'.format(
                nickname, logout_url)
        else:
            login_url = users.create_login_url('/home')
            greeting = '<a href="%s">Sign in</a>' % (login_url)
        my_template = jinja_environment.get_template("templates/sign.html")
        self.response.write(
            '<html><body>{}</body></html>'.format(greeting))


class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        login_url = users.create_login_url('/home')
        logout_url = users.create_logout_url('/home')
        if user:
            nickname = user.nickname()
            greeting = 'Welcome, {}! (<a href="{}">sign out</a>)'.format(
                nickname, logout_url)
        else:
            greeting = '<a href="%s">Sign in</a>' % (login_url)
        my_template = jinja_environment.get_template("templates/home.html")
        render_data = {
        'signin' : login_url
        }
        self.response.write(my_template.render(render_data))
        self.response.write(
            '<html><body>{}</body></html>'.format(greeting))

class HighScoreModel(ndb.Model):
    username = ndb.StringProperty()
    score = ndb.IntegerProperty()


app = webapp2.WSGIApplication([
    ('/home', MainHandler),
    ('/hangman', HangmanHandler),
    ('/highscore', HighScoreHandler),
    ('/aboutus', AboutUsHandler),
    ('/signin', MainPage),
    ('/sign', SignHandler)


], debug=True)
