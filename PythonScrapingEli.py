from optparse import Values
from bs4 import BeautifulSoup
import requests
page = requests.get("https://www.nfl.com/stats/player-stats/category/rushing/2022/reg/all/rushingyards/desc")
soup = BeautifulSoup(page.content, 'html.parser')
rushing = soup.find(class_= "d3-o-table d3-o-table--detailed d3-o-player-stats--detailed d3-o-table--sortable")
playerTable = rushing.find('tbody')
listOfStats = []
for player in playerTable:
    for stat in player.find_all('td'):
        listOfStats.append(stat.get_text())
DictPln = {}
keyThing = []
temporaryList = []
valueThing = []
for i, value in enumerate (listOfStats):
    if (i+9) % 10 == 0:
        temporaryList.append("Rush Yds: " + value)
    elif (i+8) % 10 == 0:
        temporaryList.append("ATT: " + value)
    elif (i+7) % 10 == 0:
        temporaryList.append("TD: " + value)
    elif (i+6) % 10 == 0:
        temporaryList.append("20+: " + value)
    elif (i+5) % 10 == 0:
        temporaryList.append("40+: " + value)
    elif (i+4) % 10 == 0:
        temporaryList.append("LNG: " + value)
    elif (i+3) % 10 == 0:
        temporaryList.append("Rush 1st: " + value)
    elif (i+2) % 10 == 0:
        temporaryList.append("Rush !st%: " + value)
    elif(i+1) % 10 == 0:
        temporaryList.append("Rush FUM")
    elif i % 10 == 0 and i != 0:
        keyThing.append(value.strip())
        valueThing.append(temporaryList)
        temporaryList = []
    elif i == 0:
        keyThing.append(value.strip())
zipThing = (list(zip(keyThing, valueThing)))
for item in zipThing:
    DictPln[item[0]] = item[1]
#print (DictPln["Saquon Barkley"])
while True:
    print ("who's stats would you like?")
    terminalScanner = str(input())
    if terminalScanner in keyThing:
      print (DictPln[terminalScanner])
    else:
        print("Try another name!")