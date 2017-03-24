import rauth
import time
import pandas as pd

def get_para(city, state, category, num):
    """
    Return a parameter list that can be passed to a Yelp API call given city,
    state, category (Chinese, Mexican, etc.), num (number of businesses to return)
    """
    params = {}
    params["term"] = category
    params["location"] = "{}, {}".format(city, state)
    params["category_filter"] = "restaurants"
    params["radius_filter"] = '50000'
    params["limit"] = str(num)
    params["sort"] = 2 #sort by rating
    return params

def get_business(city, state, category, num):
    """
    Given parameters return search results from Yelp API.
    """
    params = get_para(city, state, category, num)
    
    consumer_key = "FHjUV_8ZnrKQ-WX22Bb1cw"
    consumer_secret = "MSAajBT2EPztDh5I-t9PVAhxnO4"
    token = "X8ic1b2V0QVB25BqcXtL_XFI1mJo_Wy3"
    token_secret = "wTok52fM7BEYgDBDD0eqNflEiMo"

    session = rauth.OAuth1Session(
        consumer_key = consumer_key,
        consumer_secret = consumer_secret,
        access_token = token,
        access_token_secret = token_secret)
    request = session.get("http://api.yelp.com/v2/search",params=params)
    #Transforms the JSON API response into a Python dictionary
    businesses = request.json()
    session.close()
    #handle the situation where there are not enough restaurants given the requirements
    if 'businesses' not in list(businesses.keys()):
        #each category needs to have at least 6 restaurants
        if num <= 5:
            return None
        else:
            time.sleep(1.0)
            return get_business(city, state, category, num-5)
    return businesses['businesses']

def get_review(businessID):
    """
    Given a businessID (returned from get_business) return a dictionary containing
    information about the top review (review text, user id, user rating and time created).
    """
    consumer_key = "FHjUV_8ZnrKQ-WX22Bb1cw"
    consumer_secret = "MSAajBT2EPztDh5I-t9PVAhxnO4"
    token = "X8ic1b2V0QVB25BqcXtL_XFI1mJo_Wy3"
    token_secret = "wTok52fM7BEYgDBDD0eqNflEiMo"

    session = rauth.OAuth1Session(
        consumer_key = consumer_key,
        consumer_secret = consumer_secret,
        access_token = token,
        access_token_secret = token_secret)
    request = session.get("http://api.yelp.com/v2/business/"+businessID)
    data = request.json()
    session.close()
    #handle the situation where there are no reviews
    if 'reviews' not in list(data.keys()):
        return None
    data = data['reviews'][0]
    review = {}
    review['uid'] = data['user']['id']
    review['review'] = data['excerpt']
    review['urating'] = data['rating']
    review['time_created'] = data['time_created']
    return review

def generate_table(city, state, category, num, table):
    """
    Return a dictionary containing all information needed for analysis.
    One item for each restaurant and the key is restaurant id (rid, string).
    In each restaurant item, there are city (string), name (string), category (string),
    rating (float), review_count (integer), snippet_text (string), review (string),
    user id (string), user rating (float) and time_created (integer).
    """
    businesses = get_business(city, state, category, num)
    #if the current search yields no result
    if businesses == None:
        return table
    for business in businesses:
        #only add the business at the first time it is found
        if business['id'] not in list(table.index):
            business['category'] = category
            business['city'] = city
            review = get_review(business['id'])
            #add to table only if there is a review for the restaurant
            if review != None:
                table = table.append(pd.Series(get_one_entry(business, review), name=business['id']))           
    return table
        
def get_one_entry(business, review):
    """
    Given the results for one restaurant from get_business and get_review,
    put them into one dictionary (corresponding to one entry if converted to data frame).
    """
    one_entry = {}
    one_entry['city'] = business['city']
    one_entry['name'] = business['name']
    one_entry['category'] = business['category']
    one_entry['rating'] = business['rating']
    one_entry['review_count'] = business['review_count']
    one_entry['snippet_text'] = business['snippet_text']
    one_entry['review'] = review['review']
    one_entry['uid'] = review['uid']
    one_entry['urating'] = review['urating']
    one_entry['time_created'] = review['time_created']
    return one_entry
    

def test_business():
    locations = [('San Francisco','CA'),('Los Angeles','CA'),('New York', 'NY')]
    businesses = []
    for city, state in locations[:1]:
        result = get_business(city, state, 'Chinese', 5)
        businesses += result
        time.sleep(1.0)
    return businesses

def test_review(businesses):
    reviews = []
    for business in businesses:
        result = get_review(business['id'])
        if result != None:
            reviews.append(result)
        time.sleep(1.0)
    return reviews

def test_generate_table():
    locations = [('San Francisco','CA'),('Los Angeles','CA'),('Boston','Texas')]
    table = pd.DataFrame()
    for city, state in locations:
        for category in ['Chinese', 'Italian']:
            table = generate_table(city, state, category, 1, table)
    return table
    
if __name__=="__main__":
    businesses = test_business()
    reviews = test_review(businesses)
    table = test_generate_table()
    
