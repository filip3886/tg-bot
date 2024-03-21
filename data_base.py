import sqlite3 as sq
class get_and_save_info: 
    
    
    def create_table():
        connection = sq.connect('contacts.db')
        cursor = connection.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        username TEXT NOT NULL
        )
        ''')

        connection.commit()
        connection.close()

    def insert_data_to_db(id, first_name, username ):
        connection = sq.connect('contacts.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO Users (id, first_name, username) VALUES (?, ?, ?)', (id, first_name, username))
        connection.commit()
        connection.close()

    def show_db_info():
        global user
        connection = sq.connect('contacts.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Users')
        users = cursor.fetchall()
        for user in users:
            print(user)

        connection.close()
