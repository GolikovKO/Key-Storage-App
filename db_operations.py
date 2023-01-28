import os
import psycopg2


def add_record_into_database():
    os.system('clear')

    while True:
        #db_exists = False

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
                        conn = psycopg2.connect(user="postgres", password="1",
                                                host="127.0.0.1")  # TODO: refactor connection later
                        cursor = conn.cursor()
                        conn.autocommit = True
                    except:
                        print("ERROR: An error occurred while connecting to server. Check connection settings.")
                        break
                    else:
                        sql = "SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND " \
                              "table_type='BASE TABLE'"
                        cursor.execute(sql)
                        table_names = cursor.fetchall()

                        cursor.close()
                        conn.close()

                        exist_tables_names = [''.join(i) for i in table_names]

                        print(exist_tables_names)
                else:
                    print("ERROR: The database with the entered name does not exist. Check the list of existing "
                          "databases on the screen and try again.\n")
                    """conn = psycopg2.connect(user="postgres", password="1", host="127.0.0.1") # TODO: refactor connection later
                    cursor = conn.cursor()
                except:
                    print("An error occurred while connecting to servers-database.")
                    break
                else:
                    conn.autocommit = True
                    sql = "SELECT datname FROM pg_database"
                    cursor.execute(sql)
                    db_names = cursor.fetchall()

                    cursor.close()
                    conn.close()

                    exists_db_names = [''.join(i) for i in db_names]
                    print(exists_db_names)
                for db in db_names:
                    tuple_db_name_to_str = ''.join(db)
                    db_names_list.append(tuple_db_name_to_str)

                if db_name in db_names_list:
                    db_exists = True
                    cursor.close()
                    conn.close()

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
                try:
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
            print("ERROR: An error occurred while connecting to server. Check connection settings.\n")
            break
        else:
            conn.autocommit = True
            sql = "SELECT datname FROM pg_database"
            cursor.execute(sql)
            db_names = cursor.fetchall()

            for db_name in db_names:
                tuple_db_name_to_str = ''.join(db_name)
                print(tuple_db_name_to_str)
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

                print(f"\nDatabase {new_db_name} successfully created!\n")

                cursor.close()
                conn.close()
            except:
                print("An error occurred while creating the database. The database has not been created.")
                cursor.close()
                conn.close()
                break
            try:
                conn = psycopg2.connect(dbname=new_db_name, user="postgres", password="1", host="127.0.0.1")
                conn.autocommit = True
                cursor = conn.cursor()

                sql = "CREATE TABLE record ( " \
                      "name varchar(50)," \
                      "login varchar(50)," \
                      "password varchar(50)," \
                      "date varchar(50)) "
                cursor.execute(sql)

                print("\nTable record successfully created!\n")
                cursor.close()
                conn.close()
                break
            except:
                print("An error occurred while creating table in the database. Table was not created.")
                cursor.close()
                conn.close()
                break

