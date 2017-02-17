#test the functions
source("RTourest.R")
state = "California"
city = "San Francisco"
nlist = 15
show_attractions(state, city, nlist)
Aselection = '6,7'
dining_pref = 'Chinese'
radius = 2000
show_restaurants(Aselection, dining_pref, radius)
Rselection = '1'
start = "City Hall"
end = start
show_url(Rselection, start, end)

#test the shiny app
setwd(paste(getwd(),"/..",sep=""))
library(shiny)
runApp("Tourest")