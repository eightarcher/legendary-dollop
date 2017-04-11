import sqlite3

conn = sqlite3.connect('tutorial2.sql')
c = conn.cursor()
conn.close()
