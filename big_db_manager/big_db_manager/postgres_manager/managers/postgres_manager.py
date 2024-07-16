import psycopg2

from ..instances import PostgresDB
from ..instances import UserRole
from ..settings import ROOT_ROLE_NAME, ROOT_DB_NAME


class PostgresManager:
    root_user = UserRole(name=ROOT_ROLE_NAME)
    root_db = PostgresDB(name=ROOT_DB_NAME, user=root_user, host=None, port=None)

    def __init__(self, db, create_db_and_role=False, autocommit=True):
        self.db = db
        self.__autocommit = autocommit
        self.__connection, self.__cursor = None, None

        if create_db_and_role:
            root_manager = self.__class__(self.root_db)
            root_manager.cursor.execute(
                f"create role {self.db.user.name} with password '{self.db.user.password}' login;"
            )
            root_manager.cursor.execute(
                f"create database {self.db.name} owner {self.db.user.name} encoding 'utf-8';"
            )

            root_manager.close_cursor()

    @property
    def connection(self):
        if not self.__connection:
            params = {
                'dbname': self.db.name,
                'user': self.db.user.name,
            }
            if self.db.host:
                params['host'] = self.db.host
            if self.db.port:
                params['port'] = self.db.port
            if self.db.user.password:
                params['password'] = self.db.user.password

            self.__connection = psycopg2.connect(**params)
            self.__connection.autocommit = self.__autocommit
        return self.__connection

    @property
    def cursor(self):
        """
        Когда нам нужен метод, для установки объекта как атрибута класса
        можно задуматься над созданием property
        :return:
        """
        if not self.__cursor:
            self.__cursor = self.connection.cursor()
        return self.__cursor

    def close_cursor(self):
        self.__cursor.close()
        self.__cursor = None

    def close_connection(self):
        self.close_cursor()
        self.__connection.close()
        self.__connection = None

