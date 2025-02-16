def genfunc():
    print ('ilk cagri')
    yield 1
    print ('ikinci cagri')
    yield 2
def write(X):
    print(X)
a = genfunc()
print(a.__next__())
write("Ara fasıl")
y=a.__next__()
print(y)