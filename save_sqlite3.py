import sqlite3

conn = sqlite3.connect('top_cities.db') # open the file and get the connection
c = conn.cursor #get the cursor
#execute SQL sentences by exectute() method
# To get the same result if reapeat this method many times, remove the cities table if exits
c.execute("DROP TABLE IF EXITS cities")
# create a cities TABLE
c.exectute("""
    CREATE TABLE cities (
        rank integer,
        city text,
        population integer
    )

""")
