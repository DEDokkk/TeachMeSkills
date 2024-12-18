from managers.user_manager import UserManager
from settings import JSON_STORAGE
from storage.json_storage import JsonStorage
class AuthSystem:
    storage = JsonStorage(JSON_STORAGE)
    user_manager = UserManager()
    storage1 = list(storage.read())
    @classmethod
    def auth(cls):
        while True:
            email = cls.user_manager.get_email()
            password = cls.user_manager.get_password()
            for i in cls.storage1:
                if i['email'] == email and i['password'] == password:
                    print('You are welcome!')
                    return True
            print('incorrect password or email')
            continue



