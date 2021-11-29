# example of how I structure my queries files (nba_queries.py, etc.) You have to keep the same number of fields in the query or you'll have to change the indexing in scrapeData.py
# each query is structured like this: (link to the s3 URL of that query, text of the query, play for that query (On, Against, Over, Under, etc.))
nbas3queries = [
    ('https://sportsdatabase.com/mlb/query?output=default&su=1&ou=1&sdql=H&submit=++S+D+Q+L+%21++', 'H', 'On')
]
