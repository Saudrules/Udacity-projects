#!/usr/bin/env python3
import psycopg2


DBNAME = "news"


def FirstQuery():
    try:
    db = psycopg2.connect(database=DBNAME)
    except:
        print("Unable to connect to database.")
    cur = db.cursor()
    query1 = """ SELECT articles.title, COUNT(log.path) as Views
    FROM articles INNER JOIN log ON log.path
    LIKE CONCAT('%',articles.slug)
    GROUP BY title ORDER BY Views DESC LIMIT 3;
    """
    cur.execute(query1)
    r = cur.fetchall()
    print('Most popular articles: \n')
    for i in r:
        print(i[0] + ' -- ' + str(i[1]) + " views.")
    print("\n -------------------------------------------------\n")
    db.close()


def SecondQuery():
    try:
    db = psycopg2.connect(database=DBNAME)
    except:
        print("Unable to connect to database.")
    cur = db.cursor()
    query2 = """ SELECT authors.name, COUNT(log.path) as Views
    FROM articles INNER JOIN log ON log.path
    LIKE CONCAT('%',articles.slug) INNER JOIN authors
    ON articles.author = authors.id
    GROUP BY authors.name,authors.id
    ORDER BY Views DESC;
    """
    cur.execute(query2)
    r = cur.fetchall()
    print('Most popular authors: \n')

    for i in r:
        print(i[0] + ' -- ' + str(i[1]) + " views.")
    print("\n -------------------------------------------------\n")


def ThirdQuery():
    try:
    db = psycopg2.connect(database=DBNAME)
    except:
        print("Unable to connect to database.")
    cur = db.cursor()
    query3 = """
    SELECT error_reqs.requests/(reqs_per_day.requests*0.01) Percentage,
    reqs_per_day.day
    FROM reqs_per_day
    JOIN error_reqs ON error_reqs.day = reqs_per_day.day
    WHERE error_reqs.requests > reqs_per_day.requests * 0.01;
    """
    cur.execute(query3)
    r = cur.fetchall()
    print("The day with more than 1% of requests leading to errors:")
    print(str(r[0][1]) + ' -- ' + "%.2f" % r[0][0] + "% errors")


if __name__ == '__main__':
    FirstQuery()
    SecondQuery()
    ThirdQuery()
