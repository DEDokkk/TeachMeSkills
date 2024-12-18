from instances.user import User
from managers.user_manager import UserManager
from settings import JSON_STORAGE
from storage.json_storage import JsonStorage

'''Регистрация пользователя'''


class RegistrationSystem:
    storage = JsonStorage(JSON_STORAGE)
    user_manager = UserManager()
    storage1 = storage.read()
    @classmethod
    def sign_up(cls):
        while True:
            '''Проверка на наличие юзера'''
            email = cls.user_manager.get_email()
            users = cls.user_manager.get_users(cls.storage1)
            try:
                if cls.user_manager.find_by_email(email, users):
                    '''Если пользователь существует, то вызываем ошибку'''
                    raise ValueError
            except ValueError:
                print('There is already such email')
                continue
            password = cls.user_manager.get_password()
            '''Создаем юзера'''
            user = User(email, password)
            cls.storage.add_to_storage(user.dict_serialize())
            break
