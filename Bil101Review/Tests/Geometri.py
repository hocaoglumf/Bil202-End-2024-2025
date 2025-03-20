class Geometri:
    def __init__(self):
        self.name="geo"
    def Alan(self):
        return 0
class Ucgen(Geometri):
    def __init__(self):
        super().__init__()

    def Alan(self,taban,yukseklik):
        return taban*yukseklik/2

class Kare(Geometri):
    def __init__(self):
        super().__init__()

    def Alan(self, kenar):
        return kenar**2

kare=Kare()
print(kare.Alan(5))
ucgen=Ucgen()
print(ucgen.Alan(3,4))