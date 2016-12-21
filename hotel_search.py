#search within a certain radius from the attractions
hotels = []
hotel_locations = {}
hotel_urls = {}

hotel_pref = "hotel"
radius = 1000

rank = 0
while len(hotels) < n:
    for i in selection:
        coord = ya.get_coord(attraction_locations[attractions[i]])
        ht_params = ya.get_para_hotel(coord[0],coord[1],hotel_pref,radius)
        hotel = ya.get_results(ht_params)['businesses']
        if len(hotel) > 0:
            name = str(hotel[rank]['name'])
            hotels.append(name)
            hotel_locations[name] = hotel[rank]['location']['coordinate']
            hotel_urls[name] = hotel[rank]['url']
    rank += 1

selected_hotel = 2
coord = ya.get_coord(hotel_locations[hotels[selected_hotel]])
reverse_geocode_result = gmaps.reverse_geocode(coord)
start_point = reverse_geocode_result[0]['formatted_address']
