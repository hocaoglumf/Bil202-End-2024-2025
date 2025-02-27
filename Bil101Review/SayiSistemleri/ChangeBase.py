
numbers=[0,1,2,3,4,5,6,7,8,9]
for i in range(65,65+26):
    numbers.append(chr(i))

def nth(nth,lst=numbers):
    return lst[nth::nth+1][0]

def to_base(n, base):
    if n == 0:
        return "0"

    digits = []
    while n:
        dgt=str(nth(n%base))
        digits.append(dgt)
        n //= base

    return "".join(digits[::-1])


# Örnek kullanım
number = 25453
base = 18
converted = to_base(number, base)
print(f"{number} sayısı {base} tabanında: {converted}")
