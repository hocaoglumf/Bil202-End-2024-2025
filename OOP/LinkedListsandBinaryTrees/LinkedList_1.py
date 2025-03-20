''' Birbirlerine ilişkilendirilmiş nesneleri içeren listeler. '''

import random
class RandomFunction:
    def __init__(self):
        self.name="Base"
        self.linkedEntity=None

    def GenerateRandomValue(self):
        if not(self.linkedEntity==None):
            self.linkedEntity.GenerateRandomValue()
        return 9

class Normal(RandomFunction):
    def __init__(self):
        super().__init__()
        self.name="Normal"

    def GenerateRandomValue(self):
        if not(self.linkedEntity==None):
            self.linkedEntity.GenerateRandomValue()
        return random.normalvariate(20,3)

class Uniform(RandomFunction):
    def __init__(self):
        super().__init__()
        self.name="Uniform"

    def GenerateRandomValue(self):
        if not(self.linkedEntity==None):
            self.linkedEntity.GenerateRandomValue()
        return random.uniform(2,10)

class Exponential(RandomFunction):
    def __init__(self):
        super().__init__()
        self.name="Expo"

    def GenerateRandomValue(self):
        if not(self.linkedEntity==None):
            self.linkedEntity.GenerateRandomValue()
        return random.expovariate(3)

class Constant(RandomFunction):
    def __init__(self):
        super().__init__()
        self.name="Constant"


class Container:
    def __init__(self):
        self.distributions=[]

    def Attach(self, dagilim):
        if (len(self.distributions)>0):
            last=len(self.distributions)-1
            self.distributions[last].linkedEntity=dagilim
        self.distributions.append(dagilim)

    def Generate(self):
        self.distributions[0].GenerateRandomValue()

n0=Normal()
n1=Normal()
c0=Constant()
e0=Exponential()
c1=Constant()

cont=Container()

cont.Attach(n0)
cont.Attach(n1)
cont.Attach(c1)
cont.Attach(c0)
cont.Attach(e0)

cont.Generate()
e0.name="Exponential"
print("son")
