class Moving:
    def move(self):
        raise NotImplementedError


class Animal(Moving):
    def voice(self):
        raise NotImplementedError


class Transport(Moving):
    def launch(self):
        raise NotImplementedError


class Duck(Animal):
    def voice(self):
        print("Quack")

    def move(self):
        print("Swim")


class Tiger(Animal):
    def voice(self):
        print("Roar")

    def move(self):
        print("Run")


class Car(Transport):
    status = False

    def launch(self):
        self.status = not self.status
        print("Start")

    def move(self):
        if self.status != True:
            print('Stop')
        else:
            print('Move')


duck = Duck()
duck.voice()
duck.move()
tiger = Tiger()
tiger.voice()
tiger.move()
car = Car()
car.launch()
car.move()
