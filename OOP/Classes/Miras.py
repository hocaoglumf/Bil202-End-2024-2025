''' Miras mekanizması ve polymorphism (Çok biçimlilik)'''
class Arac:
    def __init__(self):
        self.tip=""
        self.marka=""
        self.maksHiz=0
        self.kapasite=0
        self.yolcuSayisi=0
    def Raporla(self):
        print("Raporum : ")
        print("Tip :",self.tip)
        print("Marka :",self.marka)
        print("Maks. Hiz: ",self.maksHiz)
        print("Kapasite: ",self.kapasite)
        print("Yolcu Sayısı: ",self.yolcuSayisi)

class Otomobil(Arac):
    def __init__(self):
        super().__init__()
        pass
    def BilgiYaz(self):
        print("Tip :",self.tip)
        print("Marka :",self.marka)
        print("Maks. Hiz: ",self.maksHiz)
        print("Kapasite: ",self.kapasite)
        print("Yolcu Sayısı: ",self.yolcuSayisi)

class Kamyon(Arac):
    def __init__(self):
        super().__init__()
        self.dingilSayisi=4
        self.tip="Kamyon"
    def Raporla(self):
        super().Raporla()
        print("Dingil Sayısı:", self.dingilSayisi)

class Tir(Kamyon):
    def __init__(self):
        super().__init__()
        self.dorseSayisi=2
        self.tip="Tır"

class Motosiklet(Arac):
    def __init__(self):
        super().__init__()
        self.maxLeanAngle=65

    def Raporla(self):
        super().Raporla()
        print("Maks. Yatma Açısı :",self.maxLeanAngle)

oto=Otomobil()
oto.marka="Togg"
oto.tip="SUV"
oto.yolcuSayisi=5

oto.BilgiYaz()
oto.Raporla()

kmyn=Kamyon()
kmyn.marka="Ford"
kmyn.Raporla()

tr=Tir()
tr.Raporla()

mt=Motosiklet()
mt.marka="Kawasaki"
mt.Raporla()

mt7=Motosiklet()
mt7.marka="Yamaha"
mt7.tip="Racer"
mt7.Raporla()

aracParki=[mt, mt7,tr, kmyn, oto]

print("----------------------")
for i in aracParki:
    i.Raporla()
print("----------------------")
