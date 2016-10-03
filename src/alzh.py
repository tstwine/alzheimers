from flask import Flask, render_template, session, redirect, url_for
from datetime import datetime
from livereload import Server
from flask import request

app = Flask(__name__)
app.debug = True


import lob
import googlemaps
import urllib2
import json


gmaps = googlemaps.Client(key='AIzaSyDfiWOHgamqEXHdbwuRwGuHrTtchT4W9Qg')
lob.api_key = 'test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc'
location = urllib2.urlopen('http://maps.googleapis.com/maps/api/place/nearbysearch/json?location=38.950576,-7674519&radius=50000&type=hospital&name=crusie&key=AIzaSyDfiWOHgamqEXHdbwuRwGuHrTtchT4W9Qg')



@app.route("/")
def home():
    return render_template('home.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method=="POST":
        addressLine1 = request.form["addressLine1"]
        addressLine2 = request.form["addressLine2"]
        city = request.form["city"]
        state = request.form["state"]
        zipCode = request.form["zipCode"]
        return render_template('home.html') 
@app.route("/alzheimersinfo") 
def alzheimers_info(type_of_alzheimers):       
            address = session['address']['address_Line1'] +' , ' + session['address']['address_Line2'] + ', ' + session['address_city'] + ', ' + session['address_state']
            city = session['address']['address_city']
            state = session['address']['address_state']
            geocode_results = gmaps.geocode(address)
            latitude = geocode_results[0]['geometry']['location']['lat']
            longitude = geocode_results[0][geometry]['location']['lng']
            weatherFile = weather(city, state)
            return render_template('city.html', stateName=state, cityName = city)


Server(app.wsgi_app).serve()
            








            




