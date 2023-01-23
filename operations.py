from models import RecordModel
from saving_record import save_record_to_file


def keyboard_handling(number):

    if number == '1':
        print("Creating start soon.")
        create_record()
    elif number == '2':
        print("Please choose your database.")
    else:
        print("Please input a valid number from functions list.")


def create_record():
    record = RecordModel()

    print("Write a record name. For example \"GitHUB account\"")
    name = input()
    record.name = name

    print("Write a login.")
    login = input()
    record.login = login

    print("Write a password.")
    password = input()
    record.password = password

    save_record_to_file(record)
