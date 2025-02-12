def carp(sayi1, sayi2):
    carpim = sayi1 * sayi2
    return carpim


sayi1 = int(input("Birinci sayıyı giriniz:"))
sayi2 = int(input("İkinci sayıyı giriniz:"))
print("Carpma fonksiyonum nerede ?. İşte burada ", carp)
print ("Çarpma sonucu ",carp(sayi1, sayi2))
y=carp(sayi1,sayi2)
print ("Çarpma sonucu ",y)
x=carp(sayi1**2,sayi2**.5)
print(x)