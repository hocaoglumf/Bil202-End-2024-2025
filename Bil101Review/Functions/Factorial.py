

def FactorialFunctional(n):
    f=1
    for i in range(1,n+1):
        f *=i
    return f

def FactorialRecursive(n):
    if n==0:
        return 1
    return n*FactorialRecursive(n-1)

f=FactorialFunctional(4)
fr=FactorialRecursive(4)
print(fr)