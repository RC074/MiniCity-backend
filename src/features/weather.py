import requests # library for making http requests

def get_weather(lat, lng):
    # get the weather based on the lat and lng
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&units=metric&appid=566a3751ea5e5a4fcc7f9671c1a83c31'
    res = requests.get(url).json()

    # the frontend will reference this table to choose which svg to use
    table = {
        'Clear': 0,
        'Clouds': 1,
        'Rain': 2,
        'Thunderstorm': 3,
        'Snow': 4,
        'Drizzle': 5,
    }
    index = 0,

    # below code to deconstruct the res obj and returns it
    try: 
        index = table[res['weather'][0]['main']]
    except KeyError:
        index = 6,
    print(res)
    return [index, str(round(float(res['main']['temp']))) + '°', res['timezone'], res['weather'][0]['description']]

if __name__ == '__main__': # for testing purposes
    print(get_weather(43.45011, -79.68292))
