class A:
    def __init__(self):
        self.ref=None

    def Yaz(self):
        print("A")
        self.ref.Yaz()

class B:
    def __init__(self):
        self.ref = None

    def Yaz(self):
        print("B")
        self.ref.Yaz()
a=A()
b=B()
a.ref=b
b.ref=a

try:
    a.Yaz()
except:
    print("hata")
