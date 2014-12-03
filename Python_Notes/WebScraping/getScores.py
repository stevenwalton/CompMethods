import urllib2
from bs4 import BeautifulSoup as BS
from pprint import pprint
import json

url = "http://www.espnfc.com/scores?date=20141118"
espnResponse = urllib2.urlopen(url)
soup = BS(espnResponse.read())

htmlteams = soup.find_all("div", {"class":"team-names"})
teams = []
for x in range(0,len(htmlteams)):
    if htmlteams[x].span.string == None: 
        teams.append(htmlteams[x].span.find('img')['alt'])

    else:
        teams.append(htmlteams[x].span.string)
for x in range(0,len(teams)):
    teams[x] = str(json.dumps(teams[x])).replace('"',"")
    pprint(teams[x])

#   What I know helps
#   scoreteam = soup.find_all('div',{'class':'team-name'})
#   scoreteam[0].span.string    # Shows team from 0 to 14?
#   str(scoreteam[100].span.find('img')['alt'])  # Shows team names for rest
#   The scores are similar formatting to this
#   
#   What does work
#   for i in range(0,10):
#       teams.append(scoreteam[i].span.string)
