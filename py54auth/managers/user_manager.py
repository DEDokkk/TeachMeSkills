from instances.user import User
from settings import JSON_STORAGE
from storage.json_storage import JsonStorage


class UserManager:
    class_user = User

    def get_email(cls):
        a = input("Enter your email:")
        if a == "ex":
            quit()
        return a

    def get_password(cls):
        a = input("Enter your password:")
        if a == "ex":
            quit()
        return a

    def get_users(self, storage):
        email_list = []
        for user in storage:
            email_list.append(user['email'])
        return email_list

    def find_by_email(self, email, email_list):
        if email in email_list:
            return True
        return False

    def create_user(self, email, password):
        return self.class_user(email, password)
