def Func(x):
    print (x,"  ",x**2)
    return x**2

liste={"3":Func(3)}

print(liste["3"])

eval("Func(2)")
