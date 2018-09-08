import psycopg2

DBNAME = "news"


def queryDB(query):
    """Query database and return query results"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results

QUERY1 = '''select articles.title,  count(*) from
    log,articles where log.path = concat('/article/', articles.slug)
    group by articles.title order by 1 desc limit 3;'''

QUERY2 = '''select authors.name, count(*) from log, articles,
    authors where log.path = concat('/article/', articles.slug)
    and articles.author = authors.id group by authors.name;'''

QUERY3 = '''select ERRORCOUNTS.date,
    cast((100.0 * ERRORCOUNTS.count)/TOTALCOUNTS.count as numeric(5, 3))
    as error_rate from (select count(*), date(time) from log where status like
    '%404%' group by date(time)) as ERRORCOUNTS,
    (select count(*), date(time) from log group by date(time)) as TOTALCOUNTS
    where ERRORCOUNTS.date = TOTALCOUNTS.date and
    (100.0 * ERRORCOUNTS.count/TOTALCOUNTS.count) > 1;'''


def printQuery1():
    results = queryDB(QUERY1)
    print("most popular three articles of all time: \n")
    for result in results:
        print(str(result[0]) + ' ---- ' + str(result[1]) + ' views')


def printQuery2():
    results = queryDB(QUERY2)
    print("most popular article authors of all time: \n")
    for result in results:
        print(str(result[0]) + ' ---- ' + str(result[1]) + ' views')


def printQuery3():
    results = queryDB(QUERY3)
    print("days with more than 1% of requests lead to errors: \n")
    for result in results:
        print(str(result[0]) + ' ---- ' + str(result[1]) + "%")

printQuery1()
printQuery2()
printQuery3()
