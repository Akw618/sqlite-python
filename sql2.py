# Create tables in the database
import sqlite3
con = sqlite3.connect("movies.db")
cd = con.cursor()
cd.execute("CREATE TABLE movie(title TEXT, genre TEXT, year INTEGER)")
con.commit()
con.close()