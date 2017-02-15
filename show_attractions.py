import sys
sys.path.append("/Users/jadezhang/Documents/2016-2017_data_science/API_project/Tourest")

import yelp_api as ya
import input_support as ins

def list_attractions(city, state, nlist):
    """
    Given the name of the city and the number of items to show (nlist),
    return the names (by key 'name' in the returned dict),
    locations (by key 'loc') and screen show names (by key 'show') of
    the most popular nlist attractions of the city.
    """
    lm_params = ya.get_para_attractions(city,state,nlist)
    result = ya.get_results(lm_params)
    attr_locs = {}
    attrs = []
    for i in range(nlist):
        business = result['businesses'][i]
        attrs.append(business['name'])
        attr_locs[business['name']] = business['location']['coordinate']
    attrs_show = ins.add_num(attrs)
    return {'name': attrs, 'loc': attr_locs, 'show': attrs_show}
