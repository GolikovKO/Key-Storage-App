import keyboard
from operations import keyboard_handling


def main():
    while True:
        print("1. Press 1 if you want to create passwords-database.\n"
              "2. Press 2 if you want to add existing database."
              "")

        keyboard.on_press(keyboard_handling)
        keyboard.wait()


if __name__ == '__main__':
    main()
