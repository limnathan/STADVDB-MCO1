import mysql.connector
import pandas as pd

def connect():
    #TODO: Add the databse details
    conn = mysql.connector.connect(
        host="host",
        user="root",
        password="",
        database="stadvdb"
    )
    return conn

def execute_query(conn, query):
    return pd.read_sql_query(query, conn)
