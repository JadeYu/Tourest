import googlemaps
gmaps = googlemaps.Client(key='AIzaSyDR5O0GRTeZn9Y1vW3ypD3aaIBSlmmJht4')

#determine optimized route 
def optimize_route(start, end, waypoints):
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

#create a url that shows the route in Google map.
def make_url(route):
    base = "https://www.google.com/maps/dir/"
    stops = list(map(lambda x: '+'.join(x.split()), route))
    specifics = '/'.join(stops)
    return base + specifics

