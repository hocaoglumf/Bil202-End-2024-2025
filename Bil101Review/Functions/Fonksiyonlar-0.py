def dogru():
    print("Tebrikler,girdiğiniz parola doğru.")


def yanlis():
    print("Üzgünüz,girdiğiniz parola yanlış.")


parola = "123456"

giris = input("Parolayı giriniz:")

if (parola == giris):
    dogru()
else:
    yanlis()

print("Bitti ")