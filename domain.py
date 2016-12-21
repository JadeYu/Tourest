import sys
sys.path.append("/Users/jadezhang/Documents/2016fall/new_insight_project/app_GUI")
import yelp_api as ya
import googlemaps
from datetime import datetime
import route_generating as rg

gmaps = googlemaps.Client(key='AIzaSyDR5O0GRTeZn9Y1vW3ypD3aaIBSlmmJht4')

# *********the user selects city, starting/ending points and the number of attractions to show**********
city = "San Francisco"
start = "SFO"
end = start
nlist = 20

lm_params = ya.get_para_attractions(city,nlist)
result = ya.get_results(lm_params)

attraction_locations = {}
attraction_urls = {}
attractions = []

#print out the names of the attractions by order of popularity
for i in range(nlist):
    business = result['businesses'][i]
    attractions.append(business['name'])
    attraction_locations[business['name']] = business['location']['coordinate']
    attraction_urls[business['name']] = business['url']
    print(business['name'])
print("---------------------------------------------------")

#**********the user selects attractions to go**********
attraction_selection = [1,5,10]
print("attractions selected:")
for i in attraction_selection:
    print(attractions[i])

print("---------------------------------------------------")

#get the best restaurant near selected attractions
restaurant_locations = {}
restaurant_urls = {}
restaurants = []

#**********the user selects dining preference and search radius ************
dining_pref = "Japanese, Chinese"
radius = 2000

for i in attraction_selection:
    coord = ya.get_coord(attraction_locations[attractions[i]])
    rt_params = ya.get_para_dining(coord[0],coord[1],dining_pref,radius)
    restaurant = ya.get_results(rt_params)['businesses']
    for j in range(min(3,len(restaurant))):
        business = restaurant[j]
        name = str(business['name'])
        if(name not in restaurants):
            restaurants.append(name)
            restaurant_locations[name] = business['location']['coordinate']
            restaurant_urls[name] = business['url']

print("restaurants nearby: ")
print(restaurants)
print("---------------------------------------------------")

#**********the user selects restaurant(s) to go**********
restaurant_selection = [2,3]

#add attractions and restaurants to waypoints
waypoint_addresses = []
for i in attraction_selection:
    coord = ya.get_coord(attraction_locations[attractions[i]])
    reverse_geocode_result = gmaps.reverse_geocode(coord)
    waypoint_addresses.append(attractions[i] + ', '+ reverse_geocode_result[0]['formatted_address'])

for j in restaurant_selection:
    coord = ya.get_coord(restaurant_locations[restaurants[j]])
    reverse_geocode_result = gmaps.reverse_geocode(coord)
    waypoint_addresses.append(restaurants[j] + ', '+ reverse_geocode_result[0]['formatted_address'])


#determine an optimized route through the selected waypoints
mode = "driving"
route = rg.optimize_route(start, end, waypoint_addresses, mode)

#**********take in an alternative route if specified by the user**********
#selected_order = []
#selected_route = list(map(lambda x: route[selected_order[x]],range(len(route))))

#make an url to show the route in google map
url = rg.make_url(route)
