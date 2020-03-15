#####################################################
##############       PURPOSE     ####################
#####################################################

# There isn't a huge purpose behind this. I just thought
# it would be neat to generate an HTML file from the 
# list of companies who are hub zone certified to see
# what it looks like in my browser

import pandas as pd 
from pandas import *

html_df = pd.read_csv('hub_zone_company_list.csv')
html_df.to_html('hub_zone_list.html')