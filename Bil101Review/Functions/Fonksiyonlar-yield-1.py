# verilen bir sayıdan başlayan ve yine verilen bir sayıya kadar bir önceki sayının
# karekökü kadar artarak ilerleyen bir döngü tanımlayın

def KarekokluDongu(start,stop):
    i =start
    while (i<=stop):
        j=i
        yield j
        i = i+ i**.5

for i in KarekokluDongu(3,50):
    print (i)