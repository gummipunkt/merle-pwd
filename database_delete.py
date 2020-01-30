import sqlite3

connection = sqlite3.connect("tresor_sql.db")  # connect database
cursor = connection.cursor()  # set cursor

# create database with uniqueID, user or email, password, storage, creation date
sql_command = """ 
DELETE FROM entries
"""
cursor.execute(sql_command)  # execute

connection.commit()
connection.close()