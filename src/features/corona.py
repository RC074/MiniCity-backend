import requests  # library for making http requests


def toURL(province): # replace space with %20 so that it's a valid url
    return province.replace(' ', '%20')


def get_covid(province):
    '''
    parameter: province
    return a list of covid data about that province
    '''

    # covid data source
    end_point = f'https://www.trackcorona.live/api/provinces/{toURL(province)}'
    # get the json response from the end point
    res = requests.get(end_point).json()
    print(end_point)
    print(res)
    if len(res['data']) == 0:
        return []
    # formatting the raw json data and returning the data: [province, confirmed, dead, recovered, last_updated]
    return [province, res['data'][0]['confirmed'], res['data'][0]['dead'], res['data'][0]['recovered'], res['data'][0]['updated'].split(' ')[0]]


if __name__ == '__main__':  # for testing purposes
    print(get_covid('ontario'))
