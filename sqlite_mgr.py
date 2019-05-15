import sqlite3
import os

cwd = os.getcwd()
sqlite_file = 'globelabsDB.sqlite'

sqlitedb = '%s\\%s' % (cwd, sqlite_file)

print("Connecting from %s" % sqlitedb)
conn = sqlite3.connect(sqlitedb)

c = conn.cursor()

# c.execute(""" CREATE TABLE subscribers (id INTEGER PRIMARY KEY, address TEXT, access_token TEXT)""")
# c.execute('INSERT INTO subscribers (address, access_token) VALUES (?, ?)', ("sample address", "sample token"))
c.execute("INSERT INTO subscribers (address, access_token) VALUES ('sample address', 'sample token')")

conn.commit()
conn.close()