import show_attractions as sa
import show_restaurants as sr
import show_url as su

#step 1, get a list of attractions
city = "Berkeley"
state = "CA"
nlist = 15
attractions = sa.list_attractions(city, state, nlist)
print(attractions['show'])

#step 2, user selects attractions to go
Aselection = '1,8,7'

#step 3, show a list of restaurants
dining_pref = 'Chinese'
radius = 2000
restaurants = sr.list_restaurants(attractions, Aselection, dining_pref, radius)
print(restaurants['show'])

#step 4, user selects restaurants
Rselection = '1'

#step 5, generate route across all destinations
start = "Downtown Berkeley Bart Station"
end = start
url = su.generate_url(city, state, start, end, attractions, Aselection, restaurants, Rselection)
print(url)
