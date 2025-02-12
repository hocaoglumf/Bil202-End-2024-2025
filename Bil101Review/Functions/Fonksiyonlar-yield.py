def YieldFun():
    for i in [1,2,3]:
        yield i*2
        print("i ",i)

d = YieldFun()

for j in d:
    print(j)
