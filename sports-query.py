import psycopg2

conn = psycopg2.connect("dbname=sports user=davidmohrmann host=/tmp/")

cur = conn.cursor()

# cur.execute("SELECT name FROM players ORDER BY name;")

print("Welcome to the University of Alabama's rushing statistics for 2015.")

while True:
    check_player = input("Would you like to check the stats of a player by name? (Y/N)").lower()
    if check_player == "y":
            player_search = input("\nWhich offensive player would you like to search for? ").lower()
            cur.execute("SELECT name FROM players WHERE name = (%s);",(player_search,))
            player_search_row = cur.fetchone()
            print(player_search_row)



# print(cur.fetchall())













# cur.execute("CREATE TABLE exercise(id serial PRIMARY KEY, name varchar, age integer); ")
# ​
# cur.execute("INSERT INTO exercise (name, age) VALUES (%s, %s)", ("Cameron", 29))
# cur.execute("INSERT INTO exercise (name, age) VALUES (%s, %s)", ("Nick", 31))
# cur.execute("INSERT INTO exercise (name, age) VALUES (%s, %s)", ("Ryan", 27))
# cur.execute("INSERT INTO exercise (name, age) VALUES (%s, %s)", ("Scott", 29))
# ​
# cur.execute("SELECT * FROM exercise;")
# ​
# cur.execute("UPDATE exercise SET age = 30 WHERE name = 'Scott';")
# cur.execute("DELETE from exercise WHERE name = 'Ryan';")
