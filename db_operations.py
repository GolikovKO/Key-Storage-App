import os
import psycopg2
from record_operations import create_record


def add_record_into_database():
    os.system('clear')

    while True:
        print("You choose to add record to database.\n")
        try:
            conn = psycopg2.connect(user="postgres", password="1", host="127.0.0.1")  # TODO: refactor connection later
            cursor = conn.cursor()
            conn.autocommit = True
        except:
            print("ERROR: An error occurred while connecting to server. Check connection settings.\n")
            break
        else:
            sql = "SELECT datname FROM pg_database"
            cursor.execute(sql)
            db_names = cursor.fetchall()

            cursor.close()
            conn.close()

            print("Available databases:")
            exist_db_names = [''.join(i) for i in db_names]
            for db in exist_db_names:
                print(f"--{db}--")

            print("\nEnter the name of the database you want to add the record to. If you want to leave input zero.")

            db_name = input()

            if db_name == '0':
                os.system('clear')
                break
            else:
                if db_name in exist_db_names:
                    try:
                        conn = psycopg2.connect(dbname=db_name, user="postgres", password="1", host="127.0.0.1")  # TODO: refactor connection later
                        cursor = conn.cursor()
                        conn.autocommit = True
                    except:
                        print("ERROR: An error occurred while connecting to server. Check connection settings.")
                        break
                    else:
                        sql = f"SELECT table_name FROM information_schema.tables WHERE table_schema NOT IN ('information_schema', 'pg_catalog') AND table_schema IN('public', '{db_name}')"
                        cursor.execute(sql)
                        table_names = cursor.fetchall()

                        exist_tables_names = [''.join(i) for i in table_names]
                        print(exist_tables_names)

                        if 'records' not in exist_tables_names:
                            print("Could not find the table for records. Input 1 if you want to add default table "
                                  "\"records\" or input 0 to exit or input the name of the table for records.\n")
                            string = input()

                            if string == '0':
                                os.system('clear')
                                break
                            elif string == '1':
                                try:
                                    conn = psycopg2.connect(dbname=db_name, user="postgres", password="1", host="127.0.0.1") # TODO: refactor connection later
                                    conn.autocommit = True
                                    cursor = conn.cursor()
                                except:
                                    print("ERROR: An error occurred while connecting to server. Check connection "
                                          "settings.")
                                    break
                                else:
                                    sql = "CREATE TABLE record ( " \
                                      "name varchar(50)," \
                                      "login varchar(50)," \
                                      "password varchar(50)," \
                                      "date varchar(50)) "
                                    cursor.execute(sql)

                                    print("Table record successfully created!\n")

                                    record = create_record()

                                    sql = f"INSERT INTO record (name, login, password, date) VALUES " \
                                          f"({record.name}, {record.login}, {record.password}, {record.date}) "

                                    print("Record successfully added!\n")

                                    cursor.close()
                                    conn.close()
                                    break
                            else:
                                try:
                                    conn = psycopg2.connect(dbname=db_name, user="postgres", password="1",
                                                            host="127.0.0.1")  # TODO: refactor connection later
                                    conn.autocommit = True
                                    cursor = conn.cursor()
                                except:
                                    print("ERROR: An error occurred while connecting to server. Check connection "
                                          "settings.")
                                    break
                                else:
                                    sql = f"CREATE TABLE {string} ( " \
                                          "name varchar(50)," \
                                          "login varchar(50)," \
                                          "password varchar(50)," \
                                          "date varchar(50)) "
                                    cursor.execute(sql)

                                    print(f"Table {string} successfully created!\n")

                                    record = create_record()

                                    sql = f"INSERT INTO {string} (name, login, password, date) VALUES " \
                                          f"({record.name}, {record.login}, {record.password}, {record.date}) "

                                    print("Record successfully added!\n")

                                    cursor.close()
                                    conn.close()
                                    break
                        else:
                            record = create_record()

                            sql = f"INSERT INTO records (name, login, password, date) VALUES " \
                                  f"('{record.name}', '{record.login}', '{record.password}', '{record.date}') "
                            cursor.execute(sql)

                            print("Record successfully added!\n")

                            cursor.close()
                            conn.close()
                            break
                else:
                    print("ERROR: The database with the entered name does not exist. Check the list of existing "
                          "databases on the screen and try again.\n")


def create_database():
    os.system('clear')
    while True:
        exists = False

        print("You choose to create a database.\n")
        print("Enter a database name.")
        new_db_name = input()

        try:
            conn = psycopg2.connect(user="postgres", password="1", host="127.0.0.1") # TODO: refactor connection later
            cursor = conn.cursor()
        except:
            os.system('clear')
            print("ERROR: An error occurred while connecting to server. Check connection settings.\n")
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

                print(f"\nDatabase \"{new_db_name}\" successfully created!\n")

                cursor.close()
                conn.close()
            except:
                print("An error occurred while creating the database. The database has not been created.")
                cursor.close()
                conn.close()
                break
            try:
                conn = psycopg2.connect(dbname=new_db_name, user="postgres", password="1", host="127.0.0.1") # TODO: refactor connection later
                conn.autocommit = True
                cursor = conn.cursor()

                sql = "CREATE TABLE records ( " \
                      "name varchar(50)," \
                      "login varchar(50)," \
                      "password varchar(50)," \
                      "date varchar(50)) "
                cursor.execute(sql)

                print("Table \"records\" successfully created!\n")
                cursor.close()
                conn.close()
                break
            except:
                print("An error occurred while creating table in the database. Table was not created.")
                cursor.close()
                conn.close()
                break
