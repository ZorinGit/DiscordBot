import sqlite3
import datetime


def create_server_entry(server_ID):
    NewEntry_combo_length = 0
    connect = sqlite3.connect('botdata.db')
    cursor = connect.cursor()
    cursor.execute("INSERT INTO botdata VALUES (?,?)", (server_ID, NewEntry_combo_length))
    connect.commit()
    connect.close()


def delete_server_entry(server_ID):
    connect = sqlite3.connect('botdata.db')
    cursor = connect.cursor()
    cursor.execute("DELETE FROM botdata WHERE server_ID = (?)", (server_ID,))
    connect.commit()
    connect.close()


def get_count(server_ID):
    connect = sqlite3.connect('botdata.db')
    cursor = connect.cursor()
    cursor.execute("SELECT combo_length FROM botdata WHERE server_ID = ?", (server_ID,))
    count = cursor.fetchone()[0]
    connect.close()
    return count


def update_count(server_ID, new_combo_length):
    connect = sqlite3.connect('botdata.db')
    cursor = connect.cursor()
    cursor.execute("UPDATE botdata SET combo_length = ? WHERE server_ID = (?)", (new_combo_length, server_ID,))
    connect.commit()
    connect.close()


def count_servers():
    connect = sqlite3.connect('botdata.db')
    cursor = connect.cursor()
    cursor.execute("SELECT count (*) FROM botdata")
    num_of_servers = cursor.fetchone()[0]
    connect.close()
    return num_of_servers


def get_all_serverIDs():
    connect = sqlite3.connect('botdata.db')
    cursor = connect.cursor()
    cursor.execute("SELECT server_ID FROM botdata")
    serverIDs_listoftuples = cursor.fetchall()
    serverIDs_list =[element[0] for element in serverIDs_listoftuples]
    connect.close()
    return serverIDs_list


def get_datetime_for_logs():
    #create est timezone
    est_timezone = datetime.timezone(datetime.timedelta(hours=-5), name='UTC-5')
    #get datetime for est timezone
    datetime_now = datetime.datetime.now(est_timezone)
    #format time stamp
    timestamp = datetime_now.strftime('%Y-%m-%d %H:%M:%S %Z')
    return timestamp