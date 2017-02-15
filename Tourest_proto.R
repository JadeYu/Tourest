library(rPython)
setwd("/Users/jadezhang/Documents/2016-2017_data_science/API_project/Tourest")

#Step 1: input state, city, #item to show and show attractions.
state = "California"
city = "San Francisco"
nlist = 20
python.assign("state", state)
python.assign("city", city)
python.assign("nlist", nlist)
python.load("show_attractions.py")
python.exec("attractions = list_attractions(city, state, nlist)")
attractions = python.get("attractions")
attractions$show

#Step 2: input attraction selection, 
Aselection = '6,7,20'
python.assign("Aselection", Aselection)

#Step 3: input dining preference, search radius and show the most popular restaurants nearby.
dining_pref = 'Chinese'
radius = 2000
python.assign("dining_pref", dining_pref)
python.assign("radius", radius)
python.exec("import show_restaurants as sr")
python.exec("restaurants = sr.list_restaurants(attractions, Aselection, dining_pref, radius)")
restaurants = python.get("restaurants")
restaurants$show

#Step 4: select restaurants
Rselection = '1,2'
python.assign("Rselection", Rselection)

#Step 5: generate an optimized route combining a start and end point and waypoints (all destinations above)
start = "City Hall"
end = start
python.assign("start", start)
python.assign("end", end)
python.exec("import show_url as su")
python.exec("url = su.generate_url(city, state, start, end, attractions, Aselection, restaurants, Rselection)")

url = python.get("url")


