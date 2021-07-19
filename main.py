import scrapeData
import nfl_queries
import nba_queries
import ncaafb_queries
import mlb_queries
import nhl_queries
import time

if __name__ == '__main__':
    sport = int(input('Enter 0 for NBA, 1 for NFL, 2 for NCAAFB, 3 for MLB, 4 for NHL: '))
    season = 2020
    months = {
            1: "Jan",
            2: "Feb", 
            3: "Mar",
            4: "Apr",
            5: "May",
            6: "Jun", 
            7: "Jul",
            8: "Aug",
            9: "Sep",
            10: "Oct",
            11: "Nov",
            12: "Dec"
        }

    if sport == 0 or sport > 3: #NBA and NHL
        month = int(input("Enter month: "))
        day = int(input("Enter day: "))
        if month >= 10:
            year = season
        else:
            year = season+1

        if day < 10:
            dayStr = f'0{day}'
        else:
            dayStr = f'{day}'

        date = f'{months.get(month)} {dayStr}, {year}'
        
        if sport == 0:
            for query in nba_queries.queries:
                try:
                    scrapeData.getNBAPlays(query, date, season)
                    time.sleep(1)
                except:
                    print(f'Error for {query[1]}')  
                    
        else:
            for query in nhl_queries.queries:
                try:
                    scrapeData.getNHLPlays(query, date, season)
                    time.sleep(1)
                except:
                    print(f'Error for {query[1]}')      

    elif sport == 1 or sport == 2: #NFL
        week = int(input('Enter week of the season: '))
        if sport == 1:
            queryList = nfl_queries.queries
        else:
            queryList = ncaafb_queries.queries

        for query in queryList:
            try:
                scrapeData.getFootballPlaysBacktesting(query, week, season)
                #scrapeData.getFootballPlays(query, week, season)
                time.sleep(1)
            except:
                print(f'Error for {query[1]}')
    
    elif sport == 3: #MLB
        month = int(input("Enter month: "))
        day = int(input("Enter day: "))
        season = 2021
        
        if day < 10:
            dayStr = f'0{day}'
        else:
            dayStr = f'{day}'

        date = f'{months.get(month)} {dayStr}, {season}'

        for query in mlb_queries.queries:
            try:
                scrapeData.getMLBPlays(query, date, season)
                time.sleep(1)
            except:
                print(f'Error for {query[1]}')

