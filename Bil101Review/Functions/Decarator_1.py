import time

def zaman_olc(fonk):
    def sarmal(*args, **kwargs):
        baslangic = time.time()
        sonuc = fonk(*args, **kwargs)
        bitis = time.time()
        print(f"{fonk.__name__} fonksiyonu {bitis - baslangic:.4f} saniye sürdü.")
        return sonuc
    return sarmal

@zaman_olc
def uzun_islem():
    time.sleep(2)
    print("Uzun işlem tamamlandı.")

uzun_islem()
