dizi=[2,1,3,4,1,0,5,1]


for i in range(len(dizi)):
    for j in range(i,len(dizi)):
        if dizi[i]>=dizi[j]:
            dizi[i], dizi[j]=dizi[j],dizi[i]

print (dizi)