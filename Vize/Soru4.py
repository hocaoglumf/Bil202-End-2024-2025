'''
Soru 4: (Puan: 15) Farklı araç tiplerine sahip bir ulaşım sisteminin basit bir simülasyonunu tasarladığınızı düşünelim. Tasarımda araçlar olacaktır ve her aracın bir adı ve maksimum hızı vardır. Sistemde iki tür araç var: Araba ve Bisiklet. Arabalar yakıt ikmali yapılabilirken bisikletler yakıt kullanmazlar. İlgili kodu yazınız.
'''

class Arac:
    def __init__(self):
        self.ad=""
        self.maxHiz=0

    def YakitIkmali(self,y):
        return 0

class Araba(Arac):

    def __init__(self):
        super().__init__()
        self.yakit=10

    def YakitIkmali(self,y):
        self.yakit +=y
        return self.yakit

class Bisiklet(Arac):
    def __init__(self):
        super().__init__()

araba0=Araba()
araba0.ad="myHonda"
araba0.YakitIkmali(20)

bisiklet0=Bisiklet()
bisiklet0.ad="Salcano"
