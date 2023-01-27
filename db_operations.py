import os
import psycopg2


def add_record_into_database():
    os.system('clear')

    while True:
        db_exists = False

        print("You choose to add record to database.\n")
        print("Enter the name of the database you want to add the record to. If you want to leave input zero.")
        db_name = input()

        if db_name == '0':
            os.system('clear')
            break
        else:
            try:
                conn = psycopg2.connect(user="postgres", password="1", host="127.0.0.1")
                cursor = conn.cursor()
            except:
                print("An error occurred while connecting to servers-database.")
                break
            else:
                conn.autocommit = True
                sql = "SELECT datname FROM pg_database"
                cursor.execute(sql)
                db_names = cursor.fetchall()

                db_names_list = []

                for db in db_names:
                    tuple_db_name_to_str = ''.join(db)
                    db_names_list.append(tuple_db_name_to_str)
                    if tuple_db_name_to_str == db_name:
                        db_exists = True
                        cursor.close()
                        conn.close()
                        break

            if not db_exists:
                os.system('clear')
                print(f"A database with name \"{db_name}\" does not exists. Try again.\n")
                cursor.close()
                conn.close()
            else:

                #print(db_names_list)
                print(db_name)
                conn = psycopg2.connect(db_name=f"{db_name}", user="postgres", password="1", host="127.0.0.1")
                cursor = conn.cursor()
                conn.autocommit = True

                sql = "SHOW TABLES"
                cursor.execute(sql)
                tables = cursor.fetchall()
                print(tables)

                cursor.close()
                conn.close()
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

        print("You choose to create a database.\n")
        print("Enter a database name.")
        new_db_name = input()

        try:
            conn = psycopg2.connect(user="postgres", password="1", host="127.0.0.1")
            cursor = conn.cursor()
        except:
            os.system('clear')
            print("An error occurred while connecting to servers-database. Probably some data is incorrect.\n")
            break
        else:
            conn.autocommit = True
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
                conn.autocommit = True
                sql = f"CREATE DATABASE {new_db_name}"

                cursor.execute(sql)

                os.system('clear')
                print(f"Database {new_db_name} successfully created!\n")

                cursor.close()
                conn.close()
            except:
                print("An error occurred while creating the database. The database has not been created.")
            break
