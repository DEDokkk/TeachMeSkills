class DataStorage:
    def __init__(self, path_file: str):
        self.path_file = path_file
        self.status = 'disconnected'
        self.content = None

    def _create_storage(self):
        file = open(self.path_file, 'w')
        print('создал новый файл')
        return file

    def connect(self):
        while True:
            try:
                file = open(self.path_file, 'r')
                print('открыл файл на чтение')
                self.status = 'connected'
                self.content = file.read()
                print(file)
                return file
            except FileNotFoundError:
                DataStorage._create_storage(self)

    def disconnect(self, file):
        file.close()
        print('закрыл файл')


class DataStorageWrite(DataStorage):

    def connect(self):
        while True:
            try:
                file = open(self.path_file, 'r+')
                print('открыл файл на чтение и дозапись')
                self.status = 'connected'
                self.content = file.read()
                return file
            except FileNotFoundError:
                DataStorage._create_storage(self)

    def append(self, file, new_content: str):
        file.write(new_content)
        self.content += new_content

    def disconnect(self, file):
        print(self.content)
        file.close()
        print(file)
        print('закрыл файл')
