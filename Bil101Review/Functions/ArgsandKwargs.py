# *args örnek
def fun(*args):
    return sum(args)

print(fun(1, 2, 3, 4))
print(fun(5, 10, 15))

# **kwargs örnek
def fun(**kwargs):
    for k, val in kwargs.items():
        val +=1
        print(k, val)

fun(a=1, b=2, c=3)
