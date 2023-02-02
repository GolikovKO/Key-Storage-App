import secrets
import string


def create_password():
    print("You choose to create a password by password-generator.")
    print("Input a length of a password you want to create.")

    while True:
        try:
            password_length = int(input())
        except:
            print("Input is not a number. Try again.")
        else:
            break

    alphabet = ''

    symbols_bool = False
    digits_symbols_bool = False
    character_symbols_bool = False

    while True:
        print("Input y if you want to include A..z symbols.")
        symbols = input()
        if symbols == 'y':
            alphabet += string.ascii_letters
            symbols_bool = True

        print("Input y if you want to include 0..9 symbols.")
        digits_symbols = input()
        if digits_symbols == 'y':
            alphabet += string.digits
            digits_symbols_bool = True

        print("Input y if you want to include ,.!' and other punctuation symbols.")
        character_symbols = input()
        if character_symbols == 'y':
            alphabet += string.punctuation
            character_symbols_bool = True

        if symbols_bool or digits_symbols_bool or character_symbols_bool is True:
            break
        else:
            print("You have not choose alphabet for a password. Try again.")

    password = ''

    for i in range(int(password_length)):
        password += ''.join(secrets.choice(alphabet))

    return password
