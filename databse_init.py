import sqlite3

#script to create a new database for the bot, run this before deploying for the first time.

connect = sqlite3.connect('botdata.db')

cursor = connect.cursor()

cursor.execute("""CREATE TABLE botdata (
        server_ID INTEGER PRIMARY KEY,
        combo_length INTEGER NOT NULL
        )""")

connect.commit()

connect.close()

print("botdata.db initialized successfully!")