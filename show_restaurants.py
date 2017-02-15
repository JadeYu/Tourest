import yelp_api as ya
import input_support as ins

def list_restaurants(attractions, selection, dining_pref, radius):
    """
    Take attraction search result (result), attraction selection (selection),
    dining preference (dining_pref) and a search radius (radius) as input.

    Return the names (by key 'name' in the returned dict),
    locations (by key 'loc') and screen show names (by key 'show') of
    the most popular restaurants near the selected attractions (up to 3 near each
    attraction).
    """
    rest_locs = {}
    rests = []
    select = ins.str2nlist(selection)
    for i in select:
        coord = ya.get_coord(attractions['loc'][attractions['name'][i]])
        rt_params = ya.get_para_dining(coord[0],coord[1],dining_pref,radius)
        result = ya.get_results(rt_params)['businesses']
        #for each attraction, select the the top 3 (or all available) restaurants within the specified radius
        for j in range(min(3,len(result))):
            business = result[j]
            name = str(business['name'])
            if(name not in rests):
                rests.append(name)
                rest_locs[name] = business['location']['coordinate']
    rest_show = ins.add_num(rests)
    return {'name':rests, 'loc':rest_locs, 'show': rest_show}

