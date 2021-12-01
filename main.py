import scrapeData
import queries_example
import time

if __name__ == '__main__':
    sport = int(input('Enter 0 for NBA, 1 for NFL, 2 for NCAAFB:'))
    season = 2021
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

    if sport == 0: #NBA
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

        date = f'{year}{month}{dayStr}'
        
        for query in queries_example.nbaS3queries:
            try:
                scrapeData.getNBAPlaysS3(query, date, season)
                time.sleep(1)
            except:
                print(f'Error for {query[1]}')    

    elif sport == 1 or sport == 2: #NFL and NCAAFB
        week = int(input('Enter week of the season: '))
        if sport == 1:
            queryList = queries_example.nflS3queries
        else:
            queryList = queries_example.ncaafbS3queries

        for query in queryList:
            try:
                scrapeData.getFootballPlaysS3(query, week, season)
                time.sleep(1)
            except:
                print(f'Error for {query[1]}')
