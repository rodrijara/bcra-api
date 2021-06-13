#!/usr/bin/env python  
import requests
from token import TOKEN

# get authorization code
url = 'https://api.estadisticasbcra.com/usd'
headers = {"Authorization": f"Bearer {TOKEN}"}

response = requests.get(url, headers=headers)

print(f'RESPONSE: {response.status_code}')

# # extract the dates and values 
# values = [dv['v'] for dv in r.json()]
# dates = [dv['d'] for dv in r.json()]

# dates_t = []
# for dv in r.json():
#     y, m, d = dv['d'].split('-')
#     dates_t.append((y, m, d))




