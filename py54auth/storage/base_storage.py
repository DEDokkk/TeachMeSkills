class BaseStorage:
    def read(self):
        raise NotImplementedError

    def save(self):
        raise NotImplementedError
