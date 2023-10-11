import psycopg2
from python_postgre.config import config

def connect():
    connection = None
    try:    
        params = config()
        print('Connecting to the postgreSQL database ...')
        connection = psycopg2.connect(**params)

        #Create a cursor
        curr = connection.cursor()
        print('PostgreSQL database version: ')
        curr.execute('SELECT version()')
        db_version = curr.fetchone()
        print(db_version)
        curr.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection terminated.')
if __name__ == "__main__":
    connect()