import requests
import json
import time
from tabulate import *
from my_apic_em_functions import *

requests.packages.urllib3.disable_warnings()
api_url = "https://sandboxapicem.cisco.com/api/v1/flow-analysis"

headers = {
 "content-type": "application/json",
 "X-Auth-Token": ticket
}

resp = requests.get(api_url, headers=headers, verify=False)
print("Status of /host request: ", resp.status_code)
if resp.status_code != 200:
    raise Exception("Status code does not equal 200. Response text: " + resp.text)
response_json = resp.json()
