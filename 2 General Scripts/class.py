class Car():
    def __init__(self, model, make, year):
        self.model = model
        self.make = make
        self.year = year
        self.position = 0

    def move(self, distance: int):
        self.position += distance
        print(f'{self.model} moved {distance} km')
        print(f'New position of {self.model} is {self.position} km')


a = Car('Golf', 'VW', 2021)
b = Car("C350","Benz", 2010)
a.move(20)
a.move(90)
b.move(30)
b.move(100)

