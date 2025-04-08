'''
Soru 2: (Puan: 15)
Bir grup öğrenci yan yana oturmaktadır. Grubun başındaki çocuk yanındakine “Bu sınav çok kolay olacak.” diyor ve sırayla öğrenciler bunu yanındakine söylüyor. En sondaki çocuk kendisine söyleneni söyledikten sonra “Bitti” diye sesleniyor. İlgili kodu yazınız.
'''

class Ogrenci:
    def __init__(self):
        self.next=None
    def Soyle(self):
        print("Bu sınav çok kolay olacak")
        if self.next==None:
            print("Bitti.")
        else:
            self.next.Soyle()

class Grup:
    def __init__(self):
        self.grup=[]

    def AddGrup(self,ogr):
        boy=len(self.grup)
        if boy==0:
            self.grup.append(ogr)
        else:
            self.grup[boy-1].next=ogr
            self.grup.append(ogr)

    def Oyun(self):
        self.grup[0].Soyle()

Ogr0=Ogrenci()
Ogr1=Ogrenci()
Ogr2=Ogrenci()
Ogr3=Ogrenci()
Ogr4=Ogrenci()
Ogr5=Ogrenci()
Ogr6=Ogrenci()

g=Grup()
g.AddGrup(Ogr0)
g.AddGrup(Ogr1)
g.AddGrup(Ogr2)
g.AddGrup(Ogr3)
g.AddGrup(Ogr4)
g.AddGrup(Ogr5)
g.AddGrup(Ogr6)

g.Oyun()
