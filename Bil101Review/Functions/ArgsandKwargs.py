# *args örnek
def fun(*args):
    print(args)
    return sum(args)

def fun2(L):
    return sum(L)

print(fun(1, 2, 3, 4))
print(fun(5, 10, 15))

# **kwargs örnek
def fun(**kwargs):
    for k, val in kwargs.items():
        val +=1
        print(k, val)

fun(a=1, b=2, c=3)
