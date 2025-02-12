
def HelloWorld():
    print ("Hello World")
    print("Merhaba Dünya")

def HelloWorldwReturn():
    return "Hello World"

def HelloWorldwParam(x):
    y="Hello world " +str(x)
    return y




print(HelloWorld) # Fonksiyonun hafızada yerleştiği adresi yazar.

HelloWorld() # fonksiyonu çağırır.

print(HelloWorld()) # return eden birşey olmadığı için None yazacak

print(HelloWorldwReturn())

x=HelloWorldwReturn()
print(x)
adres=HelloWorldwReturn
print(adres)

cevap=HelloWorldwParam(" ali")
print(cevap)

p=input("giriş yap : ")
cevap=HelloWorldwParam(p)
print(cevap)