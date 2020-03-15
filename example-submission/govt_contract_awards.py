##############################
######     PURPOSE    ########
##############################

# The purpose of this script is to reduce the csv 
# files which contain government contract awards for 
# the last three years. They currently have
# around 250 columns, but we only need about 15

##############################
######       POC      ########
##############################

# Last meaningful update = 14 March 2020
# GitHub = KentuckyBenjamin
# Email = Benjamin.Gaines@JackpotInsights.com

################################
################################
################################

#---------------------------------------------
# Import the libraries we need
#---------------------------------------------

import pandas as pd

#---------------------------------------------
# Convert 2019 full text to shorter usabale file
#---------------------------------------------

df_2019 = pd.read_csv('FY2019_All_Contracts_Full_20200314_6.csv')

df_2019_short = df_2019.filter(['historically_underutilized_business_zone_hubzone_firm',
'award_id_piid',
'recipient_duns',
'recipient_name',
'recipient_state_code',
'recipient_zip_4_code',
'award_description',
'naics_code',
'naics_description',
'sba_certified_8a_joint_venture',
'highly_compensated_officer_1_name',
'highly_compensated_officer_1_amount'
'self_certified_small_disadvantaged_business',
'small_disadvantaged_business',
'current_total_value_of_award',
'potential_total_value_of_award',
'award_description'
])

df_2019_short.to_csv('2019_contracts.csv')

#---------------------------------------------
# Convert 2018 full text to shorter usabale file
#---------------------------------------------

df_2018 = pd.read_csv('FY2018_All_Contracts_Full_20200314_5.csv')

df_2018_short = df_2018.filter(['historically_underutilized_business_zone_hubzone_firm',
'award_id_piid',
'recipient_duns',
'recipient_name',
'recipient_state_code',
'recipient_zip_4_code',
'award_description',
'naics_code',
'naics_description',
'sba_certified_8a_joint_venture',
'highly_compensated_officer_1_name',
'highly_compensated_officer_1_amount'
'self_certified_small_disadvantaged_business',
'small_disadvantaged_business',
'current_total_value_of_award',
'potential_total_value_of_award',
'award_description'
])

df_2018_short.to_csv('2018_contracts.csv')

#---------------------------------------------
# Convert 2017 full text to shorter usabale file
#---------------------------------------------

df_2017 = pd.read_csv('FY2017_All_Contracts_Full_20200314_4.csv')

df_2017_short = df_2017.filter(['historically_underutilized_business_zone_hubzone_firm',
'award_id_piid',
'recipient_duns',
'recipient_name',
'recipient_state_code',
'recipient_zip_4_code',
'award_description',
'naics_code',
'naics_description',
'sba_certified_8a_joint_venture',
'highly_compensated_officer_1_name',
'highly_compensated_officer_1_amount'
'self_certified_small_disadvantaged_business',
'small_disadvantaged_business',
'current_total_value_of_award',
'potential_total_value_of_award',
'award_description'
])

df_2017_short.to_csv('2017_contracts.csv')