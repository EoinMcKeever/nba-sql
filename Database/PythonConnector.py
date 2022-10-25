import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'Eoin',
    password = 'Gunpowder123',
    database = "nba"
)
cursor = mydb.cursor()

#cursor.execute('CREATE DATABASE nba')

cursor.execute("SHOW DATABASES")

cursor.execute("CREATE TABLE PlayerStats (name VARCHAR(255), user_name VARCHAR(255))")

