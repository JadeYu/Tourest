#create data

import pandas as pd

locations = [('San Francisco','CA'),
             ('Los Angeles','CA'),
             ('Boston','MA'),
             ('New York City', 'NY'),
             ('Seattle', 'WA'),
             ('Atlanta', 'GA')]
categories = ['Chinese', 'Italian', 'Japanese', 'Korean', 'Indian', 'Mexican', 'American (New)', 'Seafood']

table = pd.DataFrame()
nsample = 30

for city, state in locations[:1]:
    for category in categories:
        print(city, state, category)
        table = generate_table(city, state, category, nsample, table)
        
table.to_csv('San_Francisco.csv')


