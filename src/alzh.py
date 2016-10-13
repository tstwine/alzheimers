from flask import Flask, render_template, session, redirect, url_for, json
from datetime import datetime
from livereload import Server
from flask import request
#from dementia import *
# from onset import *
from distutils.core import setup 

#from modules.onset import *

import os
import lob
import googlemaps
import urllib2
import json
import functions

import onset
#import dementia

app = Flask(__name__)
app.debug = True

gmaps = googlemaps.Client(key='AIzaSyDfiWOHgamqEXHdbwuRwGuHrTtchT4W9Qg')
lob.api_key = 'test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc'
location = urllib2.urlopen('http://maps.googleapis.com/maps/api/place/nearbysearch/json?location=38.950576,-7674519&radius=50000&type=hospital&name=crusie&key=AIzaSyDfiWOHgamqEXHdbwuRwGuHrTtchT4W9Qg')
dementia = []
alzheimers = []

@app.route("/")
def home():
    dementia_data = {
        'question': 'What do you want to know about the onset of dementia?',
        'fields': ['onset', 'family_history', 'active_management', 'gender', 'education', 'race']
        }

    alzheimers_data = {
    'question': 'What do you want to know about the different types of Alzheimers?',
    'fields': ['definition, diagnosis, symptons, Types_of_Alzheimers, treatments']    
    }

    return render_template('home.html', dementia=dementia_data, alzheimers=alzheimers_data)



@app.route("/information/<subject>")
def information(subject):

    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

    if subject == 'characteristics':
        characteristics_json_url = os.path.join(SITE_ROOT, "json", "characteristics.json")
        information_dict = json.load(open(characteristics_json_url))

    elif subject == 'dementia':
        dementia_json_url = os.path.join(SITE_ROOT, "json", "dementia.json")
        information_dict = json.load(open(dementia_json_url))

    elif subject == 'alzheimers':
        alzheimers_json_url = os.path.join(SITE_ROOT, "json", "alzheimers.json")
        information_dict = json.load(open(alzheimers_json_url))


    key = request.args.get('field')
    information = information_dict[key]

    return  render_template('information.html', information=information)


if __name__ == "__main__":
    app.run(debug=True)

Server(app.wsgi_app).serve()


# var = 'red'

# if var == 'red':
#     print "Red"

# if var == 'red':
#     print "Yellow"

# elif var == 'blue':
#     print "Blue"








            




