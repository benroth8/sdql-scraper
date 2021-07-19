from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def getFootballPlays(query, currentWeek):
    queryURL = query[0]
    req = Request(queryURL , headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, "html.parser")
    summaryTable = soup.findAll("table")[2]
    gamesTable = summaryTable.findAll("table")[-1].findAll("td")
    for x in range(len(gamesTable)-16, 0, -24):
        gameq1score = gamesTable[x].text.strip()
        gameWeek = int(gamesTable[x-5].text.strip())
        if (gameq1score != ''):
            break
        if (gameq1score == '' and gameWeek == currentWeek):
            teamName = gamesTable[x-3].text.strip()
            print(f'{teamName} - {query[2]} --- {query[1]}', end = '\n')

def getFootballPlaysBacktesting(query, currentWeek, currseason):
    queryURL = query[0]
    req = Request(queryURL , headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, "html.parser")
    summaryTable = soup.findAll("table")[2]
    gamesTable = summaryTable.findAll("table")[-1].findAll("td")
    for x in range(len(gamesTable)-16, 0, -24):
        gameq1score = gamesTable[x].text.strip()
        gameWeek = int(gamesTable[x-5].text.strip())
        season = int(gamesTable[x-4].text.strip())
        if (season < currseason):
            break
        if (season == currseason and gameWeek < currentWeek):
            break
        if (gameWeek == currentWeek and season == currseason):
            teamName = gamesTable[x-3].text.strip()
            print(f'{teamName} - {query[2]} --- {query[1]}', end = '\n')

def getNBAPlays(query, date, season):
    queryURL = query[0]
    req = Request(queryURL , headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, "html.parser")
    summaryTable = soup.findAll("table")[3]
    gamesTable = summaryTable.findAll("table")[-1].findAll("td")
    for x in range(len(gamesTable)-13, 0, -20):
        score = gamesTable[x].text.strip()
        gameDate = gamesTable[x-7].text.strip()
        gameSeason = int(gamesTable[x-4].text.strip())
        if gameSeason < season:
            break
        if gameDate == date:
            teamName = gamesTable[x-3].text.strip()
            print(f'{teamName} - {query[2]} --- {query[1]}', end = '\n')

def getMLBPlays(query, date, season):
    queryURL = query[0]
    req = Request(queryURL , headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, "html.parser")
    summaryTable = soup.findAll("table")[3]
    gamesTable = summaryTable.findAll("table")[-1].findAll("td")
    for x in range(len(gamesTable)-15, 0, -19):
        team = gamesTable[x].text.strip()
        gameDate = gamesTable[x-4].text.strip()
        gameSeason = int(gameDate[-4:])
        if gameSeason < season:
            break
        if gameDate == date:
            print(f'{team} - {query[2]} --- {query[1]}', end = '\n')

def getNHLPlays(query, date, season):
    queryURL = query[0]
    req = Request(queryURL , headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, "html.parser")
    summaryTable = soup.findAll("table")[5]
    gamesTable = summaryTable.findAll("td")
    
    for x in range(len(gamesTable)-13, 0, -16):
        team = gamesTable[x].text.strip()
        gameDate = gamesTable[x-3].text.strip()
        gameSeason = int(gameDate[-4:])
        if gameSeason < season:
            break
        if gameDate == date:
            print(f'{team} - {query[2]} --- {query[1]}', end = '\n')
    