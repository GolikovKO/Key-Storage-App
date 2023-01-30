from datetime import datetime
from models import RecordModel


def create_record():
    record = RecordModel()

    print("Write a record name. For example \"GitHUB account\".")
    name = input()
    record.name = name

    print("Write a login.")
    login = input()
    record.login = login

    print("Write a password.")
    password = input()
    record.password = password

    record.date = datetime.now()

    return record
