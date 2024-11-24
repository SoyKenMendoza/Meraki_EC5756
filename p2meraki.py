import requests

from pprint import pprint

#Global Parameters

url = 'https://api.meraki.com/api/v1/organizations/'

payload = None

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

headers = {

    "Authorization": "Bearer 75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6",
    "Accept": 'application/json'
}

response = requests.request('GET', url, headers=headers, data = payload)
response.raise_for_status()
pprint(response.json())
