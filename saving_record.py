import psycopg2


def create_database():
    while True:
        exists = False

        print("Enter a database name.")
        new_db_name = input()

        try:
            conn = psycopg2.connect(dbname="postgres", user="postgres", password="1", host="127.0.0.1")
            cursor = conn.cursor()
            conn.autocommit = True
        except:
            print("An error occurred while connecting to database.")
        else:
            sql = "SELECT datname FROM pg_database"
            cursor.execute(sql)
            db_names = cursor.fetchall()

            for db_name in db_names:
                tuple_db_name_to_str = ''.join(db_name)
                if tuple_db_name_to_str == new_db_name:
                    exists = True
                    break
        if exists:
            print("A database with the same name already exists. Try again.")
            cursor.close()
            conn.close()
        else:
            try:
                sql = f"CREATE DATABASE {new_db_name}"

                cursor.execute(sql)
                print(f"Database {new_db_name} successfully created!.")

                cursor.close()
                conn.close()
            except:
                print("An error occurred while creating the database. The database has not been created.")
            break
