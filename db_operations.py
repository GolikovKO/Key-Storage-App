import os

import psycopg2


def add_record_into_database():
    os.system('clear')
    print("You choose to add record to database.\n")

    while True:
        exists = False

        print("Enter a database name. If you want to leave input zero.")
        db_name = input()

        if db_name == '0':
            break
        else:
            try:
                conn = psycopg2.connect(dbname="postgres", user="postgres", password="1", host="127.0.0.1")
                cursor = conn.cursor()
                conn.autocommit = True
            except:
                print("An error occurred while connecting to servers-database.")
                break
            else:
                sql = "SELECT datname FROM pg_database"
                cursor.execute(sql)
                db_names = cursor.fetchall()

                for db in db_names:
                    tuple_db_name_to_str = ''.join(db)
                    if tuple_db_name_to_str == db_name:
                        exists = True
                        break
            if not exists:
                os.system('clear')
                print(f"A database with name \"{db_name}\" does not exists. Try again.\n")
                cursor.close()
                conn.close()
            else:
                print("EXISTS")
                """try:
                    sql = f"CREATE DATABASE {new_db_name}"
    
                    cursor.execute(sql)
    
                    os.system('clear')
                    print(f"Database {new_db_name} successfully created!\n")
    
                    cursor.close()
                    conn.close()
                except:
                    print("An error occurred while creating the database. The database has not been created.")
                break"""


def create_database():
    os.system('clear')
    while True:
        exists = False

        print("You choose to create a database.")
        print("Enter a database name.")
        new_db_name = input()

        try:
            conn = psycopg2.connect(dbname="postgres", user="postgres", password="1", host="127.0.0.1")
            cursor = conn.cursor()
            conn.autocommit = True
        except:
            print("An error occurred while connecting to servers-database.")
            break
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

                os.system('clear')
                print(f"Database {new_db_name} successfully created!\n")

                cursor.close()
                conn.close()
            except:
                print("An error occurred while creating the database. The database has not been created.")
            break
