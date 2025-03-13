class Car:
    def __init__(self):
        self.engine=None

    def SetEnginePower(self,pwr):
        self.engine.horsepower=pwr

class Engine:
    def __init__(self):
        self.horsepower=115
        self.cyclinder=4

araba=Car()

motor=Engine()
araba.engine=motor

araba.SetEnginePower(200)

