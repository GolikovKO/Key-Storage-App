import os

from record_operations import create_record
from db_connections import execute_sql


def show_databases():
    os.system('clear')
    sql = "SELECT datname FROM pg_database"

    try:
        db_names = execute_sql(None, sql)
    except:
        print("ERROR: An error occurred while connecting to server. Check connection settings.\n")
    else:
        print("Available databases:")
        exist_db_names = [''.join(i) for i in db_names]
        for db in exist_db_names:
            print(f"--{db}--")

        print()


def delete_database():
    os.system('clear')

    while True:
        print("You choose to delete a database.\n")
        sql = "SELECT datname FROM pg_database"

        try:
            db_names = execute_sql(None, sql)
        except:
            print("ERROR: An error occurred while connecting to server. Check connection settings.\n")
            break
        else:
            print("Available databases:")
            exist_db_names = [''.join(i) for i in db_names]
            for db in exist_db_names:
                print(f"--{db}--")

            print("Enter a database name that need to be deleted. If you want to leave input zero.")
            delete_db_name = input()

            if delete_db_name == '0':
                os.system('clear')
                break
            else:
                if delete_db_name in exist_db_names:
                    sql = f"DROP DATABASE {delete_db_name}"
                    execute_sql(None, sql)
                    print("Database successfully deleted!\n")
                    break
                else:
                    print("ERROR: The database with the entered name does not exist. Check the list of existing "
                          "databases on the screen and try again.\n")


def add_record_into_database():
    os.system('clear')

    while True:
        print("You choose to add record to database.\n")

        sql = "SELECT datname FROM pg_database"

        db_names = execute_sql(None, sql)

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
                sql = f"SELECT table_name FROM information_schema.tables WHERE table_schema NOT IN (" \
                      f"'information_schema', 'pg_catalog') AND table_schema IN('public', '{db_name}') "
                table_names = execute_sql(db_name, sql)

                exist_tables_names = [''.join(i) for i in table_names]
                if 'records' not in exist_tables_names:
                    print("Could not find the table for records. Input 1 if you want to add default table "
                          "\"records\" or input 0 to exit or input the name of the table for records.\n")
                    string = input()

                    if string == '0':
                        os.system('clear')
                        break
                    elif string == '1':
                        sql = "CREATE TABLE records ( " \
                              "name varchar(50)," \
                              "login varchar(50)," \
                              "password varchar(50)," \
                              "date varchar(50)) "
                        execute_sql(db_name, sql)
                        print("Table record successfully created!\n")

                        record = create_record()
                        sql = f"INSERT INTO record (name, login, password, date) VALUES " \
                              f"('{record.name}', '{record.login}', '{record.password}', '{record.date}') "
                        execute_sql(db_name, sql)

                        print("Record successfully added!\n")
                        break
                    else:
                        sql = f"CREATE TABLE {string} ( " \
                              "name varchar(50)," \
                              "login varchar(50)," \
                              "password varchar(50)," \
                              "date varchar(50)) "
                        execute_sql(db_name, sql)
                        print(f"Table {string} successfully created!\n")

                        record = create_record()
                        sql = f"INSERT INTO {string} (name, login, password, date) VALUES " \
                              f"({record.name}, {record.login}, {record.password}, {record.date}) "
                        execute_sql(db_name, sql)

                        os.system('clear')
                        print("Record successfully added!\n")
                        break
                else:
                    record = create_record()
                    sql = f"INSERT INTO records (name, login, password, date) VALUES " \
                          f"('{record.name}', '{record.login}', '{record.password}', '{record.date}') "
                    execute_sql(db_name, sql)

                    print("Record successfully added!\n")
                    break
            else:
                print("ERROR: The database with the entered name does not exist. Check the list of existing "
                      "databases on the screen and try again.\n")


def create_database():
    os.system('clear')
    while True:
        exists = False

        print("You choose to create a database.")
        print("Enter a database name.\n")
        new_db_name = input()

        sql = "SELECT datname FROM pg_database"
        db_names = execute_sql(None, sql)

        for db_name in db_names:
            tuple_db_name_to_str = ''.join(db_name)
            if tuple_db_name_to_str == new_db_name:
                exists = True
                break

        if exists:
            print("A database with the same name already exists. Try again.\n")
        else:
            sql = f"CREATE DATABASE {new_db_name}"
            execute_sql(None, sql)
            print(f"Database \"{new_db_name}\" successfully created!\n")

            sql = "CREATE TABLE records ( " \
                  "name varchar(50)," \
                  "login varchar(50)," \
                  "password varchar(50)," \
                  "date varchar(50)) "
            execute_sql(new_db_name, sql)
            print("Default table \"records\" successfully created!\n")
            break
