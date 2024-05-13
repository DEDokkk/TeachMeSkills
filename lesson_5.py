from random import randint


def enter_range_numbers():
    print('Enter range boundaries or "exit" to exit')
    print('Range boundaries must be more than 5 ang less than 30')
    low_range = (input('Enter low range: '))
    high_range = (input('Enter high range: '))
    global range_numbers
    if low_range == 'exit' or high_range == 'exit':
        quit()
    range_numbers = [i for i in range(int(low_range), int(high_range) + 1)]
    if not low_range.isnumeric() or not high_range.isnumeric() or check_range(range_numbers) == False:
        return enter_range_numbers()
    else:
        return range_numbers


def check_range(range_numbers):
    if len(range_numbers) >= 30 or len(range_numbers) <= 5:
        return False


def randoming_numbers(range_numbers):
    random_numbers = []
    while len(random_numbers) != 3:
        random_number = (randint(range_numbers[0], range_numbers[-1]))
        if random_number in random_numbers:
            continue
        else:
            random_numbers.append(random_number)
    return random_numbers


def get_numbers(random_numbers):
    print('Enter three numbers or "exit" to exit')
    print(random_numbers)
    while len(random_numbers) != 0:
        user_number = (input('Enter number: '))
        if user_number == 'exit':
            quit()
        elif user_number.isnumeric() == False:
            print('Enter only number')
            continue
        elif int(user_number) < range_numbers[0] or int(user_number) > range_numbers[-1]:
            print('Enter number from range')
            continue
        elif int(user_number) in random_numbers:
            print('You guessed right!')
            random_numbers.remove(int(user_number))
        else:
            print('Try again')
            continue
    print('You won!')
    quit()


def ygadaika():
    range_numbers = enter_range_numbers()
    random = randoming_numbers(range_numbers)
    get_numbers(random)


print(ygadaika())
