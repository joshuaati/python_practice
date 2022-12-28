class Car():
    def __init__(self, model, make, year):
        self.model = model
        self.make = make
        self.year = year

    def move(self, distance: int):
        position = 0
        position += distance

        print(f'{self.model} moved {position} km')


a = Car('Golf', 'VW', 2021)
b = Car('S320', 'Mercedes', 2018)
a.move(20)
b.move(90)

