class PostgresDB:
    def __init__(self, name, user, host='127.0.0.1', port='5432'):
        self.name = name
        self.user = user
        self.host = host
        self.port = port
