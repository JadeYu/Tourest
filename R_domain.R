setwd("/Users/jadezhang/Documents/2016-2017_data_science/API_project/Tourest")
python.load("domain.py")

attractions <- python.get("attractions")
route_url <- python.get("url")

city = "Los Angeles"
python.assign("city", city)
start = "SFO"
end = start
nlist = 20
dining_pref = "Japanese, Chinese"
radius = 2000
attraction_selection = [1,5,10]
restaurant_selection = [2,3]
mode = "driving"


