from custom_exeptions import NotANumberError, UnknownOperationError

def calculate(x, command, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise NotANumberError

    if command not in ['+', '-', '*', '/', '**']:
        raise UnknownOperationError
    if command == '+':
        return x + y
    elif command == '**':
        return x ** y
    elif command == '-':
        return x - y
    elif command == '*':
        return x * y
    elif command == '/':
        try:
            return x / y
        except ZeroDivisionError:
            return "Division by zero is impossible"



try:
    x = float(input("Enter first number: "))
    command = input("Enter operation (+, -, *, /, **): ")
    y = float(input("Enter second number: "))
    print(calculate(x, command, y))

except NotANumberError as error:
    print(error)

except UnknownOperationError as error:
    print(error)

except Exception as error:
    print("An error has occurred:", error)