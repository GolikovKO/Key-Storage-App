from db_operations import add_record_into_database, create_database, delete_database, show_databases


def keyboard_handling(number):

    if number == '0':
        exit(0)
    elif number == '1':
        create_database()
    elif number == '2':
        print("TO DO ADD EXISTING DATABASE")
    elif number == '3':
        add_record_into_database()
    elif number == '4':
        delete_database()
    elif number == '5':
        show_databases()
    else:
        print("Please input a valid number from functions list.")
