def MySecondRange(start, stop, inc):
    i=start
    sonuc_Listesi=[]
    while (i<=stop):
        sonuc_Listesi.append(i)
        i +=1
    return sonuc_Listesi
print("Yield ile üretilen liste")

def MyRange(start, stop, inc):
    i=start
    while (i<=stop):
        yield i
        i +=1
L= MyRange(0,4,1)
for i in L:
    print(i)

print(list(L))

print("kendi hazırladığım return ile yapılan liste")
L2=MySecondRange(0,5,1)
for j in L2:
    print(j)

print(L2)