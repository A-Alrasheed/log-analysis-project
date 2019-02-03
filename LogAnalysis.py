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

