import psycopg2


def create_database():
    print("Enter a database name.")
    db_name = input()

    try:
        conn = psycopg2.connect(dbname="postgres", user="postgres", password="1", host="127.0.0.1")
        cursor = conn.cursor()

        conn.autocommit = True
        sql = f"CREATE DATABASE {db_name}"

        cursor.execute(sql)
        print("Database successfully created!.")

        cursor.close()
        conn.close()
    except:
        print("An error occurred while creating the database. The database has not been created.")
