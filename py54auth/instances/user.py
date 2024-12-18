class User:
    def __init__(self, email, password):
        self.email = email
        self.__password = password

    def dict_serialize(self):
        return {"email": self.email, "password": self.__password}
