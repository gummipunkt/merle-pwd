import sqlite3
connection = sqlite3.connect("tresor_sql.db")  # create database
cursor = connection.cursor()  # set cursor

# create database with uniqueID, user or email, password, storage, creation date
sql_command = """ 
CREATE TABLE entries ( 
unique_id INTEGER PRIMARY KEY, 
user_email VARCHAR(50), 
password VARCHAR(100),
url VARCHAR(500),
storage VARCHAR(500),
created VARCHAR(10));"""

cursor.execute(sql_command)  # execute

connection.commit()
connection.close()
