#####################################################
##############       PURPOSE     ####################
#####################################################

# The point of this script is to identify firms who have
# consistently done business with the government for three
# years in a row. 

# The desired outcome from this script is to produce a 
# dataframe of relevant info just from companies who meet
# this criteria. With such a dataframe, we could do some
# interesting modeling and analysis.

# Of note: this is simply meant to be a proof of concept. 
# This script only includes 1M records from three years 
# worth of historical data. There are many more records
# for each year. This analysis is, therefore, not exhaustive.  

# Though one could continue with the approach I've use here,
# I don't think it is the best solution. It worked for this
# hackathon. But recommendations for a more elegant, scalable solution
# to identifying firms who have consistently done business
# with the government over the last decade can be found
# in the GitHub repo. 

#####################################################
##############       CONTACT     ####################
#####################################################

# Last meaningful update = 14 March 2020
# GitHub = KentuckyBenjamin
# Email = Benjamin.Gaines@JackpotInsights.com

# ---------------------------------------------------
# Import our libraries 
# ---------------------------------------------------

import pandas as pd

# ---------------------------------------------------
# Import our data and create datframes 
# ---------------------------------------------------

df_2019 = pd.read_csv('2019_contracts.csv')
df_2018 = pd.read_csv('2018_contracts.csv')
df_2017 = pd.read_csv('2018_contracts.csv')

# ---------------------------------------------------
# Create a list of company names for each year 
# ---------------------------------------------------

company_list_2019 = df_2019['recipient_name'].tolist()
company_list_2018 = df_2018['recipient_name'].tolist()
company_list_2017 = df_2018['recipient_name'].tolist()

# ---------------------------------------------------
# Create a unique list for each year's companies
# ---------------------------------------------------

company_set_2019 = set(company_list_2019)
company_set_2018 = set(company_list_2018)
company_set_2017 = set(company_list_2017)

unique_company_list_2019 = list(company_set_2019)
unique_company_list_2018 = list(company_set_2018)
unique_company_list_2017 = list(company_set_2017)

# ---------------------------------------------------
# Create a list of companies who did business each year
# ---------------------------------------------------

selected_company_list = []
for company in unique_company_list_2017:
    if company in unique_company_list_2018:
        if company in unique_company_list_2019:
            selected_company_list.append(company)

print('Lenght of list:')
print(len(selected_company_list))

# ---------------------------------------------------
# Get some basic info from the selected companies
# ---------------------------------------------------

select_company_df = df_2019.set_index(['recipient_name'])
all_company_df = select_company_df.loc[select_company_df.index.isin(selected_company_list)]
hub_zone_company_df = all_company_df[all_company_df['historically_underutilized_business_zone_hubzone_firm'] == 't']

# ---------------------------------------------------
# Return a CSV with info on the selected companies
# ---------------------------------------------------

all_company_df.to_csv('all_company_list.csv')
hub_zone_company_df.to_csv('hub_zone_company_list.csv')