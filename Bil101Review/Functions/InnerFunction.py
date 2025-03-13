def outerFunction():
    def innerFunction():
        print(2)
        return 2
    return 1+innerFunction()



x=outerFunction()
print(x)
