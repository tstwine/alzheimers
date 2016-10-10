from flask import Flask, render_template, session, redirect, url_for
from datetime import datetime
from livereload import Server
from flask import request
#from dementia import *
from onset import *
from distutils.core import setup 

#from modules.onset import *

app = Flask(__name__)
app.debug = True


import lob
import googlemaps
import urllib2
import json
import functions
import onset



gmaps = googlemaps.Client(key='AIzaSyDfiWOHgamqEXHdbwuRwGuHrTtchT4W9Qg')
lob.api_key = 'test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc'
location = urllib2.urlopen('http://maps.googleapis.com/maps/api/place/nearbysearch/json?location=38.950576,-7674519&radius=50000&type=hospital&name=crusie&key=AIzaSyDfiWOHgamqEXHdbwuRwGuHrTtchT4W9Qg')
dementia = []

dementia_data = {
    'question': 'What do you want to know about the onset of dementia?',
    'fields' :['onset', 'family_history', 'active_management', 'gender', 'education', 'race']
}

@app.route("/")
def home():
    return render_template('home.html', data=dementia_data)

if __name__ == "__main__":
    app.run(debug=True)


Server(app.wsgi_app).serve()
            








            




