class A:
    def __init__(self):
        self.name="A"
    def Yaz(self):
        print(self.name)

class B(A):
    def __init__(self):
        super().__init__()
        self.name="B"


a=A()
b=B()
print(b.name)