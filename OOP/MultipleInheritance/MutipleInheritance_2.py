class A:
    def __init__(self, a):
        print(f"A: {a}")

class B(A):
    def __init__(self, a, b):
        A.__init__(self, a)  # doğrudan A'nın init'ini çağır
        print(f"B: {b}")

class C(A):
    def __init__(self, a, c):
        A.__init__(self, a)  # doğrudan A'nın init'ini çağır
        print(f"C: {c}")

class D(B, C):
    def __init__(self, a, b, c, d):
        C.__init__(self, a, c)  # sonra C'nin init'i
        B.__init__(self, a, b)  # önce B'nin init'i
        print(f"D: {d}")

D('a', 'b', 'c', 'd')
