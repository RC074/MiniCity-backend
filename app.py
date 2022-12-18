# flask framework to setup a server that listens for post requests and respond to them
from flask import Flask, request
from flask_cors import CORS # allow http requests
import trend, weather# import the needed modules
import os # to setup the port of the server

app = Flask(__name__)
# cors = CORS(app)

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
    # res.headers.add('Access-Control-Allow-Origin', '*')
    return res

port = int(os.environ.get('PORT', 8080)) # runs on port 8080

if __name__ == '__main__':
#     # we want the server to be multi-threaded
	app.run(threaded=True, host='0.0.0.0', port=port)

