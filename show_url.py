import yelp_api as ya
import route_generating as rg
import input_support as ins

def generate_url(city, state, start, end, attractions, Aselection, restaurants, Rselection):
    """
    Take the selected attractions (and restaurants, if selected), a starting and ending point, travel mode
    (driving, transit or walking), city and state as input.

    Return Google Map URL for the optimized route. 
    """
    start = '{}, {}, {}'.format(start, city, state)
    end = '{}, {}, {}'.format(end, city, state)
    waypoints = []
    Aselect = ins.str2nlist(Aselection)
    for a in Aselect:
        coord = ya.get_coord(attractions['loc'][attractions['name'][a]])
        waypoints.append("{}, {}, {}".format(attractions['name'][a], city, state))
    #If the user chooses to find restaurants along the route, add selected restaurants to waypoints
    Rselect = ins.str2nlist(Rselection)
    for r in Rselect:
        coord = ya.get_coord(restaurants['loc'][restaurants['name'][r]])
        waypoints.append("{}, {}, {}".format(restaurants['name'][r], city, state))
    route = rg.optimize_route(start, end, waypoints)
    url = rg.make_url(route)
    return url
