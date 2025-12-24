import mysql.connector as mysqlconn

class MySQLConnection:
    def __init__(self):
        self.get_connection = mysqlconn.connect(
            host='localhost',
            user='root',
            password='Sohail12',
            database='company_db'
        )

    def get_connection(self):
        return self.get_connection
    