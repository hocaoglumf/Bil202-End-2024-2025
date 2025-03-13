class Deneme:
    genel=5
    def __init__(self):
        self.a=1

    def Method(self):
        return self.a

    @classmethod
    def ClassMethod(cls):
        return cls.genel

    @staticmethod
    def Static(a,b):
        return a+b

a=Deneme()
ins0=Deneme()
ins0.a=5
ins0.Method()

print(Deneme.ClassMethod())
Deneme.genel=6
ins1=Deneme()
print(Deneme.genel)

print(Deneme.Static(3,5))

