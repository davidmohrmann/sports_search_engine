import csv
import psycopg2

conn = psycopg2.connect("dbname=sports user=davidmohrmann host=/tmp/")

cur = conn.cursor()

cur.execute("CREATE TABLE players(" +
            "rank serial PRIMARY KEY, name varchar, " +
            "rush_att integer, rush_yards integer, rush_avg decimal, " +
            "rush_tds integer, receptions integer, rec_yards integer, " +
            "rec_avg decimal, rec_tds integer, plays integer, yds integer, " +
            "avg decimal, tds integer); ")

with open('players.csv') as csvfile:
    bama = csv.reader(csvfile)
    next(bama)
    next(bama)
    next(bama)
    for row in bama:
        cur.execute("INSERT INTO players (rank, name, rush_att, rush_yards, " +
                    "rush_avg, rush_tds, receptions, rec_yards, rec_avg, " +
                    "rec_tds, plays, yds, avg, tds) VALUES (%s, %s, " +
                    "nullif(%s, '')::int, nullif(%s, '')::int," +
                    "nullif(%s, '')::decimal, nullif(%s, '')::int, " +
                    "nullif(%s, '')::int, nullif(%s, '')::int, " +
                    "nullif(%s, '')::decimal, nullif(%s, '')::int, " +
                    "nullif(%s, '')::int, nullif(%s, '')::int, " +
                    "nullif(%s, '')::decimal, nullif(%s, '')::int)", row)

conn.commit()

cur.close()

conn.close()
