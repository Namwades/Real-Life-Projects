def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return None

def calculator():
    print('Welcome to Calculator!')

    while True:
        print('Operations:')
        print('1. Addition')
        print('2. Subtraction')
        print('3. Multiplication')
        print('4. Division')
        print('5. Quit')

        choice = input('Enter your choice: ')

        if choice == '1':
            num1 = float(input('Enter the first number: '))
            num2 = float(input('Enter the second number: '))
            result = add(num1, num2)
            print('Result:', result)
        elif choice == '2':
            num1 = float(input('Enter the first number: '))
            num2 = float(input('Enter the second number: '))
            result = subtract(num1, num2)
            print('Result:', result)
        elif choice == '3':
            num1 = float(input('Enter the first number: '))
            num2 = float(input('Enter the second number: '))
            result = multiply(num1, num2)
            print('Result:', result)
        elif choice == '4':
            num1 = float(input('Enter the first number: '))
            num2 = float(input('Enter the second number: '))
            result = divide(num1, num2)
            if result is not None:
                print('Result:', result)
            else:
                print('Error: Division by zero')
        elif choice == '5':
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    calculator()