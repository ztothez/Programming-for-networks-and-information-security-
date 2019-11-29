#Toni Tuunainen 1.3.4.4: Option 4 - Create an App for Any API
import shodan
<<<<<<< HEAD
=======
import requests
import subprocess, smtplib, re
>>>>>>> b5e1869efee528249b2d967f89ba301c78dc9402

SHODAN_API_KEY = "oC2x0L0oDdFuhFpw6jAUMWmRMGXoCqR2"

api = shodan.Shodan(SHODAN_API_KEY)

# Lookup the host
host = api.host('198.54.116.32')

# Print general info
print("""
        IP: {}
        Organization: {}
        Operating System: {}
""".format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))

# Print all banners
for item in host['data']:
        print("""
                Port: {}
                Banner: {}

        """.format(item['port'], item['data']))
<<<<<<< HEAD
=======
#! /usr/bin/env python


url = "https://api.shodan.io/tools/myip?key={oC2x0L0oDdFuhFpw6jAUMWmRMGXoCqR2}"
json_data = requests.get(url).json()
print("My ip is: "json_data)

>>>>>>> b5e1869efee528249b2d967f89ba301c78dc9402
