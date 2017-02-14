library(rPython)
setwd("/Users/jadezhang/Documents/2016-2017_data_science/API_project/Tourest")

#Step 1: input city, #item to show and show attractions.
city = "Berkeley"
nlist = 20
python.assign("city", city)
python.assign("nlist", nlist)
python.exec("import show_attractions as sa")
python.exec("attractions = sa.list_attractions(city, nlist)")
attractions = python.get("attractions")
attractions$show

#Step 2: input attraction selection, 
Aselection = '1,5,10'

#Step 3: input dining preference, search radius and show the most popular restaurants nearby.

#First check if user wants to find restaurants nearby
dine = "Yes"
#If no, jump to Step 5.

dining_pref = 'Chinese'
radius = 2000
python.assign("Aselection", Aselection)
python.assign("dining_pref", dining_pref)
python.assign("radius", radius)
python.exec("import show_restaurants as sr")
python.exec("restaurants = sr.list_restaurants(attractions, Aselection, dining_pref, radius)")
restaurants = python.get("restaurants")
restaurants$show

#Step 4: select restaurants
Rselection = '1,2'

#Step 5 (unfinished): generate an optimized route combining a start and end point and waypoints (all destinations above)
start = "Downtown Berkeley Bart Station"
end = start
mode = "driving"


