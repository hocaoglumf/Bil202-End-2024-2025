

class Sayi:
    def __init__(self):
        self.deger=0

    def Yaz(self):
        print(self.deger)

    def __del__(self):
        print("bye")


s=Sayi()
s.deger=2
s.Yaz()

s0=Sayi()
s0.deger=5
s0.Yaz()

l=[s.deger,s0]
print(l)
del s
del s0