
''' class Tanımlama '''
import random
class Araba:
    def __init__(self):
        self.marka=""
        self.maksHiz=100
        self.yakit=10
        self.yakitTipi="Benzin"

    def Hiz(self):
        hz=random.random()*100
        print("Mevcut Hız :", hz)
        return hz




arb=Araba()
print(arb.marka)
arb.marka="Honda"
arb.maksHiz=220
arb.yakit=9
arb.yakitTipi="Gaz"

car=Araba()
car.yakitTipi="Diesel"
car.yakit=6
car.marka="Fiat"
car.maksHiz=230

print("Marka:",car.marka," Hız:",car.maksHiz," Yakıt:",car.yakit," Yakıt Tipi:",car.yakitTipi)

print("Marka:",arb.marka," Hız:",arb.maksHiz," Yakıt:",arb.yakit," Yakıt Tipi:",arb.yakitTipi)

car.Hiz()
arb.Hiz()