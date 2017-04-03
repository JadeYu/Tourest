import rauth
import time

################Yelp API related functions###########################
def get_para_attractions(city,state,num):
    """
    Get a list of parameters for attraction searching using Yelp API.
    """
    params = {}
    params["term"] = "Landmark"
    params["category_filter"] = "active,arts,religiousorgs,shopping"
    params["location"] = "{}, {}".format(city, state)
    params["limit"] = str(num)
    params["sort"] = 2 #sort by rating
    params["radius_filter"] = "5000"
    return params

def get_para_dining(lat,long,dining_pref,radius):
    """
    Get a list of parameters for restaurant searching using Yelp API.
    """
    params = {}
    params["term"] = dining_pref
    params["category_filter"] = "restaurants"
    params["ll"] = "{},{}".format(str(lat),str(long))
    params["radius_filter"] = str(radius)
    params["limit"] = "5"
    params["sort"] = 2 
    return params

def get_coord(coord):
    """
    Transform API returned coordinate information (dictionary) into a tuple (lat, long).
    """
    return coord['latitude'], coord['longitude']

def get_results(params):

    """
    Make a query on Yelp API with the specified parameters.
    """

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
    """
    Test the functions that search for restaurants using the Yelp API.
    """
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
    """
    Test the functions that search for attractions using the Yelp API.
    """
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
###############################################################

##############Google map API related functions#################
import googlemaps
gmaps = googlemaps.Client(key='AIzaSyDR5O0GRTeZn9Y1vW3ypD3aaIBSlmmJht4')


def optimize_route(start, end, waypoints):
    """
    Use the google map API to get an optimized route list given a starting point, an ending
    point and waypoints to pass through.
    """
    directions_result = gmaps.directions(start,
                                     end,
                                     waypoints = waypoints,
                                     optimize_waypoints = True)
    optimized_order = directions_result[0]['waypoint_order']
    optimized_waypoints = list(map(lambda x: waypoints[optimized_order[x]],range(len(waypoints))))
    route = []
    route.append(start)
    route[1:len(waypoints)] = optimized_waypoints
    route.append(end)
    return route


def make_url(route):
    """
    Given a route list containing all destinations in order, create a url that shows the route in Google map.
    """
    base = "https://www.google.com/maps/dir/"
    stops = list(map(lambda x: '+'.join(x.split()), route))
    specifics = '/'.join(stops)
    return base + specifics
#############################################################################

################Functions related to string manipulation#######################
def str2nlist(string):
    """
    Convert a string like '1,2,15' to a list like [1,2,15].
    
    Return the list.
    """
    i = 0
    result = []
    sn = ''
    while i < len(string):
        if string[i] != ',':
            sn += string[i]
        else:
            result.append(int(sn)-1)
            sn = ''
        i += 1
    result.append(int(sn)-1)
    return result

def deslash(lstr):
    """
    Get rid of back slashes in all strings of the given list.
    """
    for i in range(len(lstr)):
        lstr[i] = lstr[i].replace("\\","")
    return lstr
                
def add_num(names):
    """
    Add a number in front of each string element of the list.

    For example: ["Betty", "Jimmy"] will become ["1. Betty", "2. Jimmy"].

    Return the modified list.
    """
    nnames = []
    for i in range(len(names)):
        nnames.append('{}. {}'.format(str(i+1), names[i]))
    return nnames

def str2bool(string):
    """
    Convert yes/no answer to boolean true/false.
    """
    if string == "Yes":
        return True
    else:
        return False
##############################################################################

#########Functions summarizing results returned from API calls################
def list_attractions(city, state, nlist):
    """
    Given the name of the city and the number of items to show (nlist),
    return the names (by key 'name' in the returned dict),
    locations (by key 'loc') and screen show names (by key 'show') of
    the most popular nlist attractions of the city.
    """
    lm_params = get_para_attractions(city,state,nlist)
    result = get_results(lm_params)
    attr_locs = {}
    attrs = []
    for i in range(nlist):
        business = result['businesses'][i]
        attrs.append(business['name'])
        attr_locs[business['name']] = business['location']['coordinate']
    attrs_show = add_num(deslash(attrs))
    return {'name': attrs, 'loc': attr_locs, 'show': attrs_show}

def list_restaurants(attractions, selection, dining_pref, radius):
    """
    Take attraction search result (result), attraction selection (selection),
    dining preference (dining_pref) and a search radius (radius) as input.

    Return the names (by key 'name' in the returned dict),
    locations (by key 'loc') and screen show names (by key 'show') of
    the most popular restaurants near the selected attractions (up to 3 near each
    attraction).
    """
    rest_locs = {}
    rests = []
    select = str2nlist(selection)
    for i in select:
        coord = get_coord(attractions['loc'][attractions['name'][i]])
        rt_params = get_para_dining(coord[0],coord[1],dining_pref,radius)
        result = get_results(rt_params)['businesses']
        #for each attraction, select the the top 3 (or all available) restaurants within the specified radius
        for j in range(min(3,len(result))):
            business = result[j]
            name = str(business['name'])
            if(name not in rests):
                rests.append(name)
                rest_locs[name] = business['location']['coordinate']
    rest_show = add_num(deslash(rests))
    return {'name':rests, 'loc':rest_locs, 'show': rest_show}

def generate_url(city, state, start, end, attractions, Aselection, restaurants, Rselection):
    """
    Take the selected attractions (and restaurants, if selected), a starting and ending point, travel mode
    (driving, transit or walking), city and state as input.

    Return Google Map URL for the optimized route. 
    """
    start = '{}, {}, {}'.format(start, city, state)
    end = '{}, {}, {}'.format(end, city, state)
    waypoints = []
    Aselect = str2nlist(Aselection)
    for a in Aselect:
        coord = get_coord(attractions['loc'][attractions['name'][a]])
        waypoints.append("{}, {}, {}".format(attractions['name'][a], city, state))
    #If the user chooses to find restaurants along the route, add selected restaurants to waypoints
    Rselect = str2nlist(Rselection)
    for r in Rselect:
        coord = get_coord(restaurants['loc'][restaurants['name'][r]])
        waypoints.append("{}, {}, {}".format(restaurants['name'][r], city, state))
    route = optimize_route(start, end, waypoints)
    url = make_url(route)
    return url
