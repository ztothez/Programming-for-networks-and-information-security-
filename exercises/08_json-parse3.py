#Toni Tuunainen 1.3.3.6: Activity - Test the URL Request
import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "aULrPQsx1pNzm6Tn9dJJa9POwdmhXMUa"
url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})

while True:
    orig = input("Starting Location: ")
    dest = input("Destination: ")
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
