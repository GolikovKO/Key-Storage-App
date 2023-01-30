from db_operations import create_database
from record_operations import create_record
from db_operations import add_record_into_database


def keyboard_handling(number):

    if number == '0':
        exit(0)
    elif number == '1':
        create_database()
    elif number == '2':
        print("TO DO ADD EXISTING DATABASE")
    elif number == '3':
        add_record_into_database()
    else:
        print("Please input a valid number from functions list.")
