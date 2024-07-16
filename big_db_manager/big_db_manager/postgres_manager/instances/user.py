class UserRole:
    def __init__(self, name, password=None):
        self.name = name
        self.__password = password

    @property
    def password(self):
        """
        Это сделано для того, что бы в какой-либо момент времени,
        случайно или намеренно, никто не мог изменить пароль из вне.

        Если вы ошиблись, и ввели не верный пароль - создайте нового пользователя.
        """
        return self.__password
