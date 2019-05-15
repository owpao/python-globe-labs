import sqlite3
import os

cwd = os.getcwd()
sqlite_file = 'globelabsDB.sqlite'

sqlitedb = '%s\\%s' % (cwd, sqlite_file)

print("Connecting from %s" % sqlitedb)

conn = sqlite3.connect(sqlitedb)

c = conn.cursor()

c.execute(""" CREATE TABLE subscribers (id INTEGER PRIMARY KEY, address TEXT, access_token TEXT)""")

conn.close()