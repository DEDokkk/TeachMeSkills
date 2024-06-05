import json


def check_account_password(account_password):
    try:
        with open('users.json', 'r') as file:
            data = json.load(file)
            if not isinstance(data, list):
                data = []
            for user in data:
                if account_password == user['password']:
                    return account_password
    except json.JSONDecodeError:
        return False
    return False


def check_account_name(account_name):
    try:
        with open('users.json', 'r') as file:
            data = json.load(file)
            if not isinstance(data, list):
                data = []
            for user in data:
                if account_name == user['name']:
                    return False
    except json.JSONDecodeError:
        return True
    return account_name


def create_account():
    account_name = input('Enter your name: ')
    if not check_account_name(account_name):
        print('There is already account with that name')
        return False
    account_password = input('Enter your password: ')
    account_age = input('Enter your age: ')
    to_json = {'name': account_name, 'password': account_password, 'age': account_age}
    try:
        with open('users.json', 'r') as file:
            data = json.load(file)
            if not isinstance(data, list):
                data = []
    except json.JSONDecodeError:
        data = []
    data.append(to_json)
    with open('users.json', 'w') as file:
        json.dump(data, file, indent=4)
        print('Your account has been created')



def change_age(account_name, account_password):
    if check_account_name and check_account_password:
        account_age = input('Enter your age: ')
        try:
            with open('users.json', 'r') as file:
                data = json.load(file)
                for user in data:
                    if user['name'] == account_name and user['password'] == account_password:
                        user['age'] = account_age
        except Exception:
            print('There is no such account')
            return False
        with open('users.json', 'w') as file:
            json.dump(data, file, indent=4)
            print('Your age has been changed')


def main():
    print('Hello! Do you have an account?')
    answer = input().lower()
    if answer == 'y':
        account_name = input('Enter your name: ')
        account_password = input('Enter your password: ')
        if check_account_name(account_name) and check_account_password(account_password):
            print('You are successfully signed in')
            while True:
                print('Do you want to change your age? Print exit if you want to log out')
                answer = input()
                if answer == 'change':
                    change_age(account_name, account_password)
                elif answer == 'exit':
                    print('You are log out')
                    break
        else:
            print('There is no such account')
            return False
    elif answer == 'n':
        print('Let"s create a new account')
        create_account()


main()