import pyTourest as pT
#step 1, get a list of attractions
city = "San Francisco"
state = "CA"
nlist = 15
attractions = pT.list_attractions(city, state, nlist)
print(attractions['show'])

#step 2, user selects attractions to go
Aselection = '1,9'

#step 3, show a list of restaurants
dining_pref = 'Chinese'
radius = 2000
restaurants = pT.list_restaurants(attractions, Aselection, dining_pref, radius)
print(restaurants['show'])

#step 4, user selects restaurants
Rselection = '1'

#step 5, generate route across all destinations
start = "City Hall"
end = start
url = pT.generate_url(city, state, start, end, attractions, Aselection, restaurants, Rselection)
print(url)
