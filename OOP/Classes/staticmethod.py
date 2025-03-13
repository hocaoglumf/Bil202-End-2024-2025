class Matematik:
    @staticmethod
    def topla(a, b):
        return a + b

# Nesne oluşturmadan çağırabiliriz
print(Matematik.topla(3, 5))  # Çıktı: 8

# Nesne oluşturarak da çağırabiliriz ama gerek yok
m = Matematik()
print(m.topla(10, 20))  # Çıktı: 30
