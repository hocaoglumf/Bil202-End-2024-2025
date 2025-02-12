def dogru():
    print("Tebrikler,girdiğiniz parola doğru.")


def yanlis():
    print("Üzgünüz,girdiğiniz parola yanlış.")


parola = "123456"

while (True):
    giris = input("Parolayı giriniz:")
    if (parola == giris):
        dogru()
        break
    else:
        yanlis()

print("Bitti ")