import sqlite3

conn = sqlite3.connect("factbook.db")
c = conn.cursor()

c.execute("SELECT name FROM facts WHERE population != '' ORDER BY population ASC LIMIT 10;")

print(c.fetchall())