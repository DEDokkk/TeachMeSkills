from random import randint

def enter_range_numbers():
    print('Enter range boundaries or "exit" to exit')
    print('Range boundaries must be more than 5 ang less than 30')
    try:
        low_range = int(input('Enter low range: '))
        high_range = int(input('Enter high range: '))
    except ValueError:
        print('Enter only numbers')
        return enter_range_numbers()
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


def get_users_numbers(random_numbers, range_numbers):
    print('Enter three numbers or "exit" to exit')
    cnt = 0
    print(random_numbers)
    for i in range(3):
        try:
            user_number = int(input('Enter number: '))
        except ValueError:
            print('Enter only number')
            continue
        if user_number == 'exit':
            quit()
        elif user_number.isnumeric() == False:
            print('Enter only number')
            continue
        elif int(user_number) < range_numbers[0] or int(user_number) > range_numbers[-1]:
            print('Enter number from range')
            continue
        elif int(user_number) in random_numbers:
            cnt += 1
    print(f'You guessed {cnt} out of 3 numbers!')
    if cnt != len(random_numbers):
        return get_users_numbers(random_numbers, range_numbers)
    else:
        quit()


def ygadaika():
    range_numbers = enter_range_numbers()
    random = randoming_numbers(range_numbers)
    get_users_numbers(random, range_numbers)


print(ygadaika())