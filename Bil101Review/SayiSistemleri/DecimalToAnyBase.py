
''' İnsanlar 10'a ayrılır ikili sayı sistemini bilenler ve bilmeyenler
'''


numbers=[0,1,2,3,4,5,6,7,8,9]
for i in range(65,91):
    numbers.append(chr(i))

def reverse_string(s):
    sr=""
    for i in range(len(s)-1,-1,-1):
        sr +=s[i]
    return sr


def Decimal2AnyBase(n,base):
    number=""
    while n:
        m=n%base
        n //=base
        number+=str(numbers[m])
    nmbr=reverse_string(number)
    return nmbr

print(Decimal2AnyBase(135,13))
