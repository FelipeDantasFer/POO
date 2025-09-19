#triangulo e a base * altura / 2 

class Triangulo():
    def __init__(self):
        self.b = 0
        self.h = 0

    def calc_area(self):
        return self.b * self.h / 2

t = Triangulo()

t.b = 10

t.h = 5

print(t.calc_area())