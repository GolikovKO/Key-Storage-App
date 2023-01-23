def save_record_to_file(record):
    with open("database.txt", "w") as file:
        string = f"{record.name} {record.login} {record.password}"
        file.write(string)
