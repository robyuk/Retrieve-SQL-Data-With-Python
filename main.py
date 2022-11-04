#! /usr/bin/env /usr/bin/python3
# Reads from a SQLITE database
db='database.db'
import sqlite3

# Establish a connection to the database
con=sqlite3.connect(db)

# Create a cursor object
cur=con.cursor()

# Run some SQL queries
# Get all rows, columns and order by asn
cur.execute("SELECT * FROM 'ips' ORDER BY asn")
print(cur.fetchall(),'\n')

# Get only address and domain columns
cur.execute("SELECT address,domain FROM 'ips' ORDER BY asn")
print(cur.fetchall(),'\n') # cur.fetchall() returns a list of tuples, each tuple is a row

#Get only rows where the asn is less than 300
cur.execute("SELECT * FROM 'ips' WHERE asn < 300")
print(cur.fetchall(),'\n')

#Get only rows where the asn is less than 300 and domain ends with 'sa'
cur.execute("SELECT * FROM 'ips' WHERE asn < 300 AND domain LIKE '%sa'")
for row in cur.fetchall():
  print(row)
       
# Note that if we try to use fetchall() agaain we get an empty list.  This is because the cursor is at the end. Run another cur.execute to reset the cursor
print(cur.fetchall())