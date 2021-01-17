from gettext import install

import numpy
import pip

import requests
res = requests.get('https://ipinfo.io/')
data = res.json()
print(data)
city = data['city']
location = data['loc'].split(',')
latitude = location[0]
longitude = location[1]
print("Latitude : ", latitude)
print("Longitude : ", longitude)
print("City: ",city)