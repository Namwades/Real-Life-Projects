import string
import random

def generate_password(length, include_lower=True, include_upper=True, include_digits=True, include_special=True):
    characters = ''
    if include_lower:
        characters += string.ascii_lowercase
    if include_upper:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    if not characters:
        return 'Error: No character types selected'

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    print('Welcome to Password Generator!')

    while True:
        length = int(input('Enter the desired password length: '))

        include_lower = input('Include lowercase letters? (y/n): ').lower() == 'y'
        include_upper = input('Include uppercase letters? (y/n): ').lower() == 'y'
        include_digits = input('Include digits? (y/n): ').lower() == 'y'
        include_special = input('Include special characters? (y/n): ').lower() == 'y'

        password = generate_password(length, include_lower, include_upper, include_digits, include_special)

        print('Generated Password:', password)
        print()

        choice = input('Generate another password? (y/n): ').lower()

        if choice != 'y':
            break

if __name__ == '__main__':
    password_generator()