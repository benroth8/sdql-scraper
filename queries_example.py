# example of how I structure my queries files (nba_queries.py, etc.) You have to keep the same number of fields in the query for each sport or you'll have to change the indexing in scrapeData.py
# each query is structured like this: (link to the s3 URL of that query, text of the query, play for that query (On, Against, Over, Under, etc.))
# Obviously these aren't real queries I would bet on
nbas3queries = [
    ('https://s3.sportsdatabase.com/NBA/query.html?sdql=Record%28%28points-o%3Apoints%2C0%2C100%29%29+as+%27SU+Record%27%2CRecord%28%28points-o%3Apoints%2Bline%2C1.91%2C100%29%29+as+%27ATS+Record%27%2CRecord%28%28points%2Bo%3Apoints-total%2C1.91%2C100%29%29+as+%27OU+Record%27%2Cdate%2Cday%2Cseason%2Csite%2Cteam%2Co%3Ateam%2Cpoints%2Co%3Apoints%2Cline%2Ctotal%2Cmargin%2Cats+margin%2Cats+margin%3E0+as+%27ATS+result%27%2Cou+margin%2Cou+margin%3E+0+as+%27OU+result%27%40season+%3D+2021+and+H%7C&submit=++S+D+Q+L+%21++', "season = 2021 and H", 'On')
]

nfls3queries = [
    ('https://s3.sportsdatabase.com/NFL/query.html?sdql=Record%28%28points-o%3Apoints%2C0%2C100%29%29+as+%27SU+Record%27%2CRecord%28%28points-o%3Apoints%2Bline%2C1.91%2C100%29%29+as+%27ATS+Record%27%2CRecord%28%28points%2Bo%3Apoints-total%2C1.91%2C100%29%29+as+%27OU+Record%27%2Cdate%2Cday%2Cweek%2Cseason%2Csite%2Cteam%2Co%3Ateam%2Cpoints%2Co%3Apoints%2Cline%2Ctotal%2Cmargin%2Cats+margin%2Cats+margin%3E0+as+%27ATS+result%27%2Cou+margin%2Cou+margin%3E+0+as+%27OU+result%27%40season+%3D+2021+and+H%7C&submit=++S+D+Q+L+%21++', "season = 2021 and H", 'Against')
]

ncaafbs3queries = [
    ('https://s3.sportsdatabase.com/NCAAFB/query.html?sdql=Record%28%28points-o%3Apoints%2C0%2C100%29%29+as+%27SU+Record%27%2CRecord%28%28points-o%3Apoints%2Bline%2C1.91%2C100%29%29+as+%27ATS+Record%27%2CRecord%28%28points%2Bo%3Apoints-total%2C1.91%2C100%29%29+as+%27OU+Record%27%2Cdate%2Cday%2Cweek%2Cseason%2Csite%2Cteam%2Co%3Ateam%2Cpoints%2Co%3Apoints%2Cline%2Ctotal%2Cmargin%2Cats+margin%2Cats+margin%3E0+as+%27ATS+result%27%2Cou+margin%2Cou+margin%3E+0+as+%27OU+result%27%40season+%3D+2021+and+H%7C&submit=++S+D+Q+L+%21++', "season = 2021 and H", 'Over')
]
