



def RemoveRepeated(dizi):
    d = []
    for i in range(len(dizi) - 1):
        if dizi[i] not in d:
            d.append(dizi[i])
    dizi = d
    return dizi

print(RemoveRepeated([2,1,3,4,1]))