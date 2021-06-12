import mysql.connector
from mysql.connector import errorcode


try:
    config = mysql.connector.connect(
        user='root',
        passwd='',
        host='127.0.0.1',
        database='contact_book'
    )
    cursor = config.cursor()
    query_sel = ('SELECT * FROM contacts')
    cursor.execute(query_sel)
    result = cursor.fetchall()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Bad password or username")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    config.close()
