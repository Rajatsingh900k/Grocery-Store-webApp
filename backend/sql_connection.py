# import mysql connector to connect with the data base.
import mysql.connector

__cnx = None
def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='Rajat@0000',
                                host='127.0.0.1',
                                database='grocery_store')
    return __cnx