import rauth
import time

def get_para_attractions(city,state,num):
    params = {}
    params["term"] = "Landmark"
    params["location"] = "{}, {}".format(city, state)
    params["limit"] = str(num)
    params["sort"] = 2 #sort by rating
    params["radius_filter"] = "5000"
    return params

#Category can be Arts & Entertainment, Active Life, or Food

def get_para_dining(lat,long,dining_pref,radius):
    params = {}
    params["term"] = dining_pref
    params["category_filter"] = "food"
    params["ll"] = "{},{}".format(str(lat),str(long))
    params["radius_filter"] = str(radius)
    params["limit"] = "5"
    params["sort"] = 2 
    return params

def get_para_hotel(lat,long,hotel_pref,radius):
    params = {}
    params["term"] = hotel_pref
    params["category_filter"] = "hotelstravel"
    params["ll"] = "{},{}".format(str(lat),str(long))
    params["radius_filter"] = str(radius)
    params["limit"] = "8"
    params["sort"] = 2 
    return params

def get_coord(coord):
    return coord['latitude'], coord['longitude']

def get_results(params):

    consumer_key = "FHjUV_8ZnrKQ-WX22Bb1cw"
    consumer_secret = "MSAajBT2EPztDh5I-t9PVAhxnO4"
    token = "X8ic1b2V0QVB25BqcXtL_XFI1mJo_Wy3"
    token_secret = "wTok52fM7BEYgDBDD0eqNflEiMo"

    session = rauth.OAuth1Session(
        consumer_key = consumer_key,
        consumer_secret = consumer_secret,
        access_token = token,
        access_token_secret = token_secret)
    request = session.get("http://api.yelp.com/v2/search",params=params)
    #Transforms the JSON API response into a Python dictionary
    data = request.json()
    session.close()

    return data

def test_dining():
    locations = [(39.98,-82.98),(42.24,-83.61),(41.33,-89.13)]
    api_calls = []
    for lat,long in locations:
        params = ya.get_para_dining(lat,long)
        result = ya.get_results(params)
        api_calls.append(result)
        print(result)
        #rate-limit
        time.sleep(1.0)
    return api_calls

def test_attractions():
    inputs = [("San Francisco","Art & Entertainment"),("San Francisco","Active Life"),("San Francisco","Food")]
    api_calls = []
    for city,category in inputs:
        params = get_para_attractions(city,category)
        result = get_results(params)
        api_calls.append(result)
        print(result)
        #rate-limit
        time.sleep(1.0)
    return api_calls

if __name__=="__main__":
    test_dining()
    test_attractions()

#result['businesses'][0]['name']
