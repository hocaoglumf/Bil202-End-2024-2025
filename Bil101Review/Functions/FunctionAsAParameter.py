def apply(func, value):
	return func(value)

def square(x):
	return x ** 2

result = apply(square, 5)
print(result) # Output: 25
