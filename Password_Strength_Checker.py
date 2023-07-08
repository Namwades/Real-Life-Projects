import re

def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'\d', password):
        score += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1

    if score <= 2:
        return 'Weak'
    elif score == 3:
        return 'Moderate'
    else:
        return 'Strong'

def password_strength_checker():
    print('Welcome to Password Strength Checker!')

    password = input('Enter a password: ')

    strength = check_password_strength(password)

    print(f'Password Strength: {strength}')

if __name__ == '__main__':
    password_strength_checker()