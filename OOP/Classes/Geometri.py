import math
class Geometri:
    def __init__(self):
        self.tip="Geometri"

class Dortgen(Geometri):
    def __init__(self):
        super().__init__()
        self.tip="Dortgen"
        self.a=0

class Kare(Dortgen):
    def __init__(self):
        super().__init__()
        self.tip="Kare"

    def Alan(self):
        return self.a**2

class Ucgen(Geometri):
    def __init__(self):
        super().__init__()
        self.tip="Ucgen"
        self.taban=0
        self.yukseklik=0

    def Alan(self):
        return self.taban*self.yukseklik/2

class Dikdortgen(Dortgen):
    def __init__(self):
        super().__init__()
        self.b=0
        self.tip="Dikdortgen"

    def Alan(self):
        return self.a*self.b

class Daire(Geometri):
    def __init__(self):
        super().__init__()
        self.tip="Daire"
        self.r=0

    def Alan(self):
        return math.pi*self.r**2

liste=[]

d0=Daire()
d0.r=5
liste.append(d0)

d1=Daire()
d1.r=7
liste.append(d1)

u0=Ucgen()
u0.taban=4
u0.yukseklik=6
liste.append(u0)

u1=Ucgen()
u1.taban=4
u1.yukseklik=6
liste.append(u1)

k0=Kare()
k0.a=9
liste.append(k0)

k1=Dikdortgen()
k1.a=9
k1.b=8

liste.append(k1)
print(liste)


for i in liste:
    print(i.tip,"  ",i.Alan())

