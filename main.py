from operations import keyboard_handling


def main():
    try:
        while True:
            print("1. Input 1 if you want to create passwords-database.\n"
                  "2. Input 2 if you want to add existing database."
                  "")
            operation = input()
            
            keyboard_handling(operation)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
