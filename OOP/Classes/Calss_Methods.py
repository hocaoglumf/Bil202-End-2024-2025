class Fabrika:
    urun_sayisi = 0  # Sınıfa ait değişken

    def __init__(self, isim):
        self.isim = isim
        Fabrika.urun_sayisi += 1  # Sınıf değişkenini artır

    @classmethod
    def toplam_urun(cls):
        return f"Toplam ürün sayısı: {cls.urun_sayisi}"

# Nesne oluşturalım
f1 = Fabrika("Telefon")
f2 = Fabrika("Bilgisayar")

# Sınıf metodu nesne oluşturmadan çağrılabilir
print(Fabrika.toplam_urun())  # Çıktı: Toplam ürün sayısı: 2
