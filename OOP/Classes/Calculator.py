class Calculator:
    def Factorial(self, n):
        if n ==0:
            return 1
        return n*self.Factorial(n-1)

    def Fibonacci(self,n):
        if n==0 or n==1:
            return 1
        return self.Fibonacci(n-1)+self.Fibonacci(n-2)
N=5
f=Calculator()
f0=f.Factorial(N)
fib0=f.Fibonacci(N)
print(str(N)+"! = ", f0, "  ", N, ". Fibonacci",fib0)