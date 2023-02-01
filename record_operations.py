from datetime import datetime
from models import RecordModel
from password_generator import create_password


def create_record():
    record = RecordModel()

    print("Write a record name. For example \"GitHUB account\".")
    name = input()
    record.name = name

    print("Write a login.")
    login = input()
    record.login = login

    print("Password settings.\n")
    while True:
        print("If you want to create a password manually input 0. If you want to use a password-generator input 1.")
        number = input()
        if number == '0':
            print("Input a password:")
            password = input()
            record.password = password
            break
        elif number == '1':
            record.password = create_password()
            break
        else:
            print("Please input a correct digit.")

    record.date = datetime.now()

    return record
