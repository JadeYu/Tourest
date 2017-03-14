#test the functions
setwd("/Users/jadezhang/Documents/2016-2017_data_science/API_project/Tourest")
source("RTourest.R")
state = "California"
city = "San Francisco"
nlist = 15
show_attractions(state, city, nlist)
#number 8 in san francisco has \ in name
Aselection = '2, 4'
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