'''
Soru 7: (Puan: 20) Bir e-ticaret sisteminde farklı türde ürünler satılmaktadır: Kitap, Elektronik Ürün ve Giyim. Her ürünün ortak özellikleri olmakla birlikte, türlerine göre bazı farklı davranışları vardır. Bu sistemde ürünlerin fiyatını hesaplayan, ürünleri listeleyen ve indirim uygulayan bir yapı geliştirilmek istenmektedir.
İstenenler:
1.	Urun adında temel (base) bir sınıf oluşturunuz.
o	Ortak nitelikler: isim, temel_fiyat
o	Metot: NetFiyat ()
2.	Aşağıdaki sınıflar Urun sınıfından türetilsin:
o	Kitap:
	Ek özellik: yazar ismi
	NetFiyat(): Kitaplara %5 vergi eklenecek
o	Electronik:
	Ek özellik: garanti_suresi
	NetFiyat (): %18 KDV + 1 yıl fazladan garanti için %3 artış
o	Giysi:
	Ek özellik: size (boyut)
	NetFiyat (): Eğer ürün indirime girdiyse %10 indirim uygulansın
3.	Urun nesnelerinden oluşan bir liste oluşturun ve bu listedeki her ürünün:
o	Adını
o	Türünü (type(Urun).__isim__)
o	Son fiyatını (NetFiyat())
ekrana yazdıran bir fonksiyon yazınız.
'''
class Urun:
    def __init__(self):
        self.isim=""
        self.temelFiyat=0

    def NetFiyat(self):
        return self.temelFiyat

class Kitap(Urun):
    def __init__(self):
        super().__init__()

    def NetFiyat(self):
        return self.temelFiyat*1.05

class Elektronik(Urun):
    def __init__(self):
        super().__init__()
        self.garanti_Suresi=1

    def NetFiyat(self):
        if self.garanti_Suresi>1:
            self.temelFiyat *=1.03
        return self.temelFiyat*1.18

class Giysi(Urun):
    def __init__(self):
        super().__init__()
        self.size=1

    def NetFiyat(self):
        return self.temelFiyat*.90

k0=Kitap()
k0.isim="Yüzüklerin Efendisi"
k0.temelFiyat=10

k1=Kitap()
k1.temelFiyat=20

e0=Elektronik()
e0.temelFiyat=200
e0.garanti_Suresi=3

e1=Elektronik()
e1.temelFiyat=400
e1.garanti_Suresi=0.5

g0=Giysi()
g0.temelFiyat=300

print(k0.NetFiyat())
print(k1.NetFiyat())
print(e0.NetFiyat())
print(e1.NetFiyat())

print(g0.NetFiyat())
