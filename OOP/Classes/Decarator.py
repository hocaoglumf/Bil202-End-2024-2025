def decorate_message(fun):
	# Nested function
	def addWelcome(site_name):
		return "Welcome to " + fun(site_name)
	# Decorator returns a function
	return addWelcome

@decorate_message
def site(site_name):
    print("in Site")
    return site_name

# Driver code
# This call is equivalent to call to
# decorate_message() with function
# site("GeeksforGeeks") as parameter
print (site("GeeksforGeeks"))
print(site("deneme"))
