library(rPython)

show_attractions <- function(state, city, nlist){
	python.assign("state", state)
	python.assign("city", city)
	python.assign("nlist", nlist)
	python.load("show_attractions.py")
	python.exec("attractions = list_attractions(city, state, nlist)")
	attractions = python.get("attractions")
	char2table(attractions$show, 3)
}

show_restaurants <- function(Aselection, dining_pref, radius){
	python.assign("Aselection", Aselection)
	python.assign("dining_pref", dining_pref)
	python.assign("radius", radius)
	python.exec("import show_restaurants as sr")
	python.exec("restaurants = 	sr.list_restaurants(attractions, Aselection, dining_pref, radius)")
	restaurants = python.get("restaurants")
	char2table(restaurants$show)
}

char2table <- function(items, ncol=1){
	tb = data.frame(matrix(items,length(items)/ncol,ncol), row.names=NULL)
	if(ncol==1){
		names(tb) = "Restaurant"
	}else{
		names(tb) = c("Top 1-5", "Top 6-10", "Top 11-15")
	}
	tb
}

show_url <- function(Rselection, start, end){
	python.assign("Rselection", Rselection)
	python.assign("start", start)
	python.assign("end", end)
	python.exec("import show_url as su")
	python.exec("url = su.generate_url(city, state, start, end, attractions, Aselection, restaurants, Rselection)")
	python.get("url")
}