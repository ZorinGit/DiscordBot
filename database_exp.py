import sqlite3
import csv

# exports botdata.db in this folder as readable botdata.csv
# must be in bot folder!


#getting data from botdata.db

connect = sqlite3.connect('botdata.db')
cursor = connect.cursor()
#get header as column names
cursor.execute('PRAGMA table_info(botdata)')
header = cursor.fetchall()
column_names = [info[1] for info in header]
#get the rest of the table
cursor.execute("SELECT * FROM botdata")
database_listOftuples = cursor.fetchall()
connect.close()

#writing data to botdata.csv

with open('botdata.csv', 'w', newline='') as botdata_csv:
    writer = csv.writer(botdata_csv)
    #write the header
    writer.writerow(column_names)
    #write the rest of the table
    for tuple_row in database_listOftuples:
        writer.writerow(tuple_row)

print("export to botdata.csv completed successfully!")