from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def getFootballPlaysS3(query, currentWeek, season):
    queryURL = query[0]
    req = Request(queryURL , headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, "html.parser")
    gamesTable = soup.findAll("table")[3].findAll("td")
    for x in range(len(gamesTable)-14, 0, -19):
        week = int(gamesTable[x].text.strip())
        gameSeason = int(gamesTable[x+1].text.strip())
        team = gamesTable[x+3].text.strip()
        if (gameSeason < season):
            break
        if (week == currentWeek):
            print(f'{team} - {query[2]} --- {query[1]}', end = '\n')
   
def getNBAPlaysS3(query, date, season):
    queryURL = query[0]
    req = Request(queryURL , headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, "html.parser")
    gamesTable = soup.findAll("table")[3].findAll("td")
    for x in range(len(gamesTable)-15, 0, -18):
        gameDate = gamesTable[x].text.strip()
        gameSeason = int(gamesTable[x+2].text.strip())
        if gameDate == date:
            teamName = gamesTable[x+4].text.strip()
            print(f'{teamName} - {query[2]} --- {query[1]}', end = '\n')
        if gameSeason < season:
            break
