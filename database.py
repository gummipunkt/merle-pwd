import sqlite3
connection = sqlite3.connect("tresor_sql.db")  # create database
cursor = connection.cursor()  # set cursor

# create database with uniqueID, user or email, password, storage, creation date
sql_command = """ 
CREATE TABLE entries ( 
unique_id INTEGER PRIMARY KEY, 
user_email VARCHAR(50), 
password VARCHAR(100),
url VARCHAR(255),
storage VARCHAR(255),
created VARCHAR(10));"""

cursor.execute(sql_command)  # execute

connection.commit()
connection.close()
