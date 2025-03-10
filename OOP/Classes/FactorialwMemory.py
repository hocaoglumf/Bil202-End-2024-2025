class Factorial:
    def __init__(self):
        self.factorials={0:1}

    def Calculate(self,n):
        if n in self.factorials:
            return self.factorials[n]
        self.factorials[n]=n*self.Calculate(n-1)
        return self.factorials[n]

ff=Factorial()
ff.Calculate(3)
ff.Calculate(4)
ff.Calculate(2)

ff0=Factorial()
ff0.Calculate(5)

print(ff.factorials)
print(ff0.factorials)