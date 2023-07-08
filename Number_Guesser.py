import random

def number_guesser():
    target_number = random.randint(1, 10)
    attempts = 0

    print('Welcome to Number Guesser!')
    print('I have generated a random number between 1 and 100.')
    print('Try to guess the number!')

    while True:
        user_guess = int(input('Enter your guess: '))
        attempts += 1

        if user_guess < target_number:
            print('Higher! Try again.')
        elif user_guess > target_number:
            print('Lower! Try again.')
        else:
            print(f'Congratulations! You guessed the number in {attempts} attempts.')
            break

if __name__ == '__main__':
    number_guesser()