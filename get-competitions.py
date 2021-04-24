#!/opt/local/bin/python
"""
 File name: get-competitions.py
 Date:      2020/11/18 15:43
 Author:    Nigel Houghton <wutang@warpten.net>
 $Id$
 Copyright: (c) Nigel Houghton 2020
"""

# This script pulls the available competitions and prints their
# associated IDs into a markdown table.

import json
import requests

url = "https://football-web-pages1.p.rapidapi.com/competitions.json"

querystring = {"include":"rounds"}

headers = {
    'x-rapidapi-key': "YOUR_API_KEY",
    'x-rapidapi-host': "football-web-pages1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
data = response.json()

# Uncomment the next line to see all the data in JSON format
# print(json.dumps(data, indent=4))

print("| Competition | Id |")
print("| --- | --- |")
for comp in data['competitions']:
    print("|",comp['generic-name'],"|",comp['id'],"|")
