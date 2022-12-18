# flask framework to setup a server that listens for post requests and respond to them
from flask import Flask, request
from flask_cors import CORS # allow http requests
from features import trend, weather, corona # import the needed modules
import os # to setup the port of the server

app = Flask(__name__)
cors = CORS(app)

@app.route('/', methods=['POST']) # the below function will handle any post requests to the server
def index():
    # store the post requests information in data in json format
    data = request.get_json(force=True)

    # deconstruct the data
    city = data['city'].split(' ')[0]
    country = data['country']
    province = data['province']

    # for debugging purposes
    print(city, country, province)

    # use each module to retrieve data

    # tweets
    tweetsIDs = trend.get_tweets(f'{city} {country}')

    # weather data
    weatherInfo = weather.get_weather(data['lat'], data['lng'])

    # covid data
    # covidData = corona.get_covid(country)

    # construct the above data into json format and returns it
    res = {
        'tweets': tweetsIDs,
        'weather': weatherInfo,
        # 'corona': covidData,
    }

    # returning the data is basically answering the post request
    return res



