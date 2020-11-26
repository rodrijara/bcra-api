#!/usr/bin/env python  
import requests

# get authorization code
with open('data/token.txt') as file: token = file.read()
url = 'https://api.estadisticasbcra.com/usd'
headers = {"Authorization": f"Bearer {token}"}

r = requests.get(url, headers=headers)

print(f'RESPONSE: {r.status_code}')

# extract the dates and values 
values = [dv['v'] for dv in r.json()]
dates = [dv['d'] for dv in r.json()]

dates_t = []
for dv in r.json():
    y, m, d = dv['d'].split('-')
    dates_t.append((y, m, d))




