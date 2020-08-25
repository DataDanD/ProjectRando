# Import the modules
import requests
import json
import csv
import pandas as pd



def Params(df):
    # Define my parameters of the search
    PARAMETERS = {
                 # 'term': 'ice cream',
                 'limit': 50,
                 'offset': df.shape[0],
                 'radius': 40000,
                 'location': 'Denver'}





if name = 'mail':
# Import past pulls
df = pd.read_csv(r'C:\Users\dan.meurer\Desktop\Working\IceIceBaby\Ice_Cream_America.csv')

# Define a business ID
business_id = '4AErMBEoNzbk7Q8g45kKaQ'
unix_time = 1546047836

# Define my API Key, My Endpoint, and My Header
API_KEY = 'xVdnshN_AjYXSabywZS0eQyE9QEpTEyZ2tYoAKG7P_5gkRERQ_92h4GDslIsQT6V0lWv2yPIOldmLzpO8BnpFc0Db6eK_sgaeh5u6Wg0sfM5iNVMP_uMovOBh7u9XnYx'
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % API_KEY}




# Make a request to the Yelp API
response = requests.get(url = ENDPOINT,
                        params = PARAMETERS,
                        headers = HEADERS)

# Convert the JSON String
business_data = response.json()

# # print the response
# print(json.dumps(business_data, indent = 3))

df = pd.DataFrame(business_data['businesses']).append(df, sort=False)


df.to_csv(r'C:\Users\dan.meurer\Desktop\Working\IceIceBaby\Ice_Cream_America.csv'
         ,index=False)


 # Ice_Cream_America = pd.DataFrame(business_data['businesses'])
 df
