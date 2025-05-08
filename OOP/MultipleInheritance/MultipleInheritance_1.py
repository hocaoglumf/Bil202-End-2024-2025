# Base class1
class Mother:
	mothername = ""
	def mother(self):
		print(self.mothername)

# Base class2
class Father:
	fathername = ""
	def father(self):
		print(self.fathername)

# Derived class
class Son(Mother, Father):
	def parents(self):
		print("Baba :", self.fathername)
		print("Anne :", self.mothername)


# Driver's code
s1 = Son()
s1.fathername = "Ahmet"
s1.mothername = "Ayşe"
s1.parents()

s2 = Son()
s2.fathername = "Ali"
s2.mothername = "Fatma"
s2.parents()