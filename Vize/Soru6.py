class SayisalIslem:
    def __init__(self, n):
        self.n = n
        self.liste = self._liste_uret()

    def _liste_uret(self):
        return [i**2 % 7 for i in range(self.n, self.n + 5)]

    def gizemli_hesap(self):
        sonuc = 0
        for i, sayi in enumerate(self.liste):
            if i % 2 == 0:
                sonuc += sayi
            else:
                sonuc -= sayi
        return sonuc

# Kullanım:
islem = SayisalIslem(3)
print(islem.gizemli_hesap())
