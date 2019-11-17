#Toni Tuunainen 1.3.3.8: Activity - Test Status and URL Print Commands

import urllib.parse
import requests

main_api = "https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400&formatted=0"
json_data = requests.get(main_api).json()
print(json_data)
