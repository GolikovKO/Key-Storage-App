import os

from input_operations import keyboard_handling


def main():
    try:
        while True:
            print("0. Input 0 if you want to exit.\n"
                  "1. Input 1 if you want to create passwords-database.\n"
                  "2. Input 2 if you want to add existing database.\n"
                  "3. Input 3 if you want to add a record into database.\n"
                  )
            number = input()

            keyboard_handling(number)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
