import pyodbc
from .PropertyUtil import PropertyUtil

class DBConnection:
    def __init__(self):
        print("Connecting to the Database.....")
        conn_str = PropertyUtil.get_property_string()
        print("coonection string fetched is:")
        print(conn_str)
        self.conn = pyodbc.connect(conn_str)
        print("Attempting...")
        print(self.conn)
        self.cursor = self.conn.cursor()
        print(self.cursor)

    def close(self):
        self.cursor.close()
        self.conn.close()