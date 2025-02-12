def genfunc():
    print ('ilk cagri')
    yield 1
    print ('ikinci cagri')
    yield 2
def write(X):
    print(X)
a = genfunc()
a.__next__()
write("Ara fasıl")
a.__next__()