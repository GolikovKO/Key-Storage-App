import secrets
import string


def create_password():
    print("You choose to create a password by password-generator.")
    print("Input a length of a password you want to create.")

    password_length = input()

    alphabet = ''

    print("Input y if you want to include A..z symbols.")
    symbols = input()
    if symbols == 'y':
        alphabet += string.ascii_letters

    print("Input y if you want to include 0..9 symbols.")
    digits_symbols = input()
    if digits_symbols == 'y':
        alphabet += string.digits

    print("Input y if you want to include ,.!' and other punctuation symbols.")
    character_symbols = input()
    if character_symbols == 'y':
        alphabet += string.punctuation

    password = ''

    for i in range(int(password_length)):
        password += ''.join(secrets.choice(alphabet))

    return password




