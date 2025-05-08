class A:
    def metot(self):
        print("A sınıfının metodu")

class B:
    def metot(self):
        print("B sınıfının metodu")

class C(A, B):  # C hem A'dan hem B'den türemiş
    def metot(self):
        print("C sınıfının metodu")
        A.metot(self)  # A'daki metot
        B.metot(self)  # B'deki metot

c=C()
c.metot()

b=B()
b.metot()