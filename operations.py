from models import RecordModel
from saving_record import create_database
from datetime import datetime


def keyboard_handling(number):

    if number == '1':
        create_database()
    elif number == '2':
        print("Please choose your database.")
    elif number == '3':
        create_record()
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

    record.date = datetime.now()

