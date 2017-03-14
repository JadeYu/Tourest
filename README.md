##Tourest

**An application built using both Python and R (shiny).**

By submitting and processing the responses of API queries to Yelp and Google Map, Tourest helps people make day tour plans through a few clicks:
  1. input city and state
  2. select attractions
  3. select restaurants

The application provides the following services:
  1. recommend attractions and restaurants based distance and Yelp reviews
  2. generate an optimized route through all destinations (attractions and restaurants) visualized on Google Map

Prototype can be accessed by running the following in R:

```
library(shiny)
runGitHub("Tourest", "JadeYu")
```

Before running the above, you need to install two python modules ([rauth](https://rauth.readthedocs.io/en/latest/) and [googlemaps](https://github.com/googlemaps/google-maps-services-python)) and one R package ([shiny](https://shiny.rstudio.com/)).
