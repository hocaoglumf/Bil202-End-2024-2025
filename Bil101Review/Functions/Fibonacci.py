def fibonacci(n):
    if n == 1:
        return 0  # Fibonacci(1) = 0
    elif n == 2:
        return 1  # Fibonacci(2) = 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)  # Rekürsif çağrı

class Fibonacci():
    def __init__(self):
        pass
    def GetFibonacci(self,n):
        if n == 1:
            return 0  # Fibonacci(1) = 0
        elif n == 2:
            return 1  # Fibonacci(2) = 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)  # Rekürsif çağrı

f=Fibonacci()
print(f.GetFibonacci(7))
