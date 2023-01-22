def keyboard_handling(event):
    operation = event.name

    if operation == '1':
        print("Creating start soon.")
    elif operation == '2':
        print("Please choose your database.")
    else:
        print("Please input a valid number from functions list.")
