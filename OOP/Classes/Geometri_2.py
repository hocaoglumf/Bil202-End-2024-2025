import math
class Geometri:
    def __init__(self):
        self.tip="Geometri"

class Dortgen(Geometri):
    def __init__(self):
        super().__init__()
        self.tip="Dortgen"

class Kare(Dortgen):
    def __init__(self):
        super().__init__()
        self.tip="Kare"

    def Alan(self,a):
        return a**2

class Ucgen(Geometri):
    def __init__(self):
        super().__init__()
        self.tip="Ucgen"

    def Alan(self, taban,yukseklik):
        return taban*yukseklik/2

class Dikdortgen(Dortgen):
    def __init__(self):
        super().__init__()
        self.tip="Dikdortgen"

    def Alan(self, a, b):
        return a*b

class Daire(Geometri):
    def __init__(self):
        super().__init__()
        self.tip="Daire"

    def Alan(self, r):
        return math.pi*r**2


d0=Daire()
print(d0.Alan(5))

d1=Daire()
print(d0.Alan(7))

u0=Ucgen()
print(u0.Alan(4,5))

u1=Ucgen()
print(u1.Alan(7,5))

k0=Kare()
print(k0.Alan(5))

k1=Dikdortgen()
print(k1.Alan(4,5))



