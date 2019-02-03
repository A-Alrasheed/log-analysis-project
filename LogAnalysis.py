#!/usr/bin/env python3

import psycopg2

DBNAME = "news"


def db_handler(function):
    """Handles database connection and operations for other functions."""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(function)
    result = c.fetchall()
    db.close()
    return result


def get_popular_articles():
    """Return the most poular three articles of all time."""

    query = """SELECT articles.title, COUNT(*) as views
               FROM articles, log
               WHERE log.path ILIKE '%' || articles.slug
               GROUP BY articles.title
               ORDER BY views desc
               LIMIT 3"""
    rows = db_handler(query)
    for row in rows:
        print(row)
