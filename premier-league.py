#!/opt/local/bin/python
# 
# Premier League Widget for Ubersicht
#
# Copyright: Nigel Houghton <wutang@warpten.net>
# $Id$
#

import urllib.request
import json
import requests

# Competition defaults to the English Premier League, ID 1.
# See README.md for list of other competitions, change the
# COMP_ID here if you want a different competition
COMP_ID = 1
url = "https://football-web-pages1.p.rapidapi.com/league-table.json"
querystring = {"team":"1","comp":COMP_ID}
headers = {
    'x-rapidapi-key': "YOUR_API_KEY",
    'x-rapidapi-host': "football-web-pages1.p.rapidapi.com"
    }
response = requests.request("GET", url, headers=headers, params=querystring)
data = response.json()
mightiest = "MY_TEAM_NAME"
print ("<table><tr><th>POS</th><th>CLUB</th><th>PD</th><th>GD</th><th>PTS</th></tr>")
for club in data['league-table']['teams']:
    name = club['name']
    pos = club['position']
    played = club['all-matches']['played']
    GD = club['all-matches']['goal-difference']
    points = club['total-points']
    if name == mightiest:
         print ("<tr>","<td class=\"mightyclass\">",pos,"</td><td class=\"mightiest\">",name,"</td><td class=\"mightyclass\">",played,"</td><td class=\"mightyclass\">",GD,"</td><td class=\"mightyclass\">",points,"</td>","</tr>")
    else:
         print ("<tr>","<td class=\"numbers\">",pos,"</td><td>",name,"</td><td class=\"numbers\">",played,"</td><td class=\"numbers\">",GD,"</td><td class=\"numbers\">",points,"</td>","</tr>")
print ("</table>")
