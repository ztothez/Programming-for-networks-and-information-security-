#Toni Tuunainen 1.3.3.8: Activity - Test Status and URL Print Commands

import urllib.parse
import requests

url = "https://api.sunrise-sunset.org/json?lat=48.8584&lng=2.2945"

json_data = requests.get(url).json()
print(json_data)
