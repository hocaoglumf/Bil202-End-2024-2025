'''
Soru 3: (Puan: 20) Bir ikili ağaç yapısında kök nesne sahip olduğu deger özniteliğinin değerini ve değerin logaritmasını alt nesne deger ve deger logaritmalarıyla toplamaktadır.  Kodu yazınız.
'''
import math
class Agac:
    def __init__(self):
        self.sol=None
        self.sag=None
        self.value=1

    def Add(self,node):
        if self.sol==None:
            self.sol=node
        elif self.sag==None:
            self.sag=node

    def Topla(self):
        if self.sol==None:
            return self.value+math.log(self.value)
        else:
            left=self.sol.Topla()
            right=self.sag.Topla()
            return self.value +math.log(self.value)+ left+right

    def SetNodes(self,left,right):
        self.sol=left
        self.sag=right

a0=Agac()
a0.value=1
a1=Agac()
a1.value=3
a2=Agac()
a2.value=5
a3=Agac()
a3.value=8
a4=Agac()
a4.value=7
a5=Agac()
a5.value=12
a6=Agac()
a6.value=10

#a0.sol=a1
#a0.sag=a2
a0.SetNodes(a1,a2)
a1.sol=a3
a1.sag=a4
a2.sol=a5
a2.sag=a6
print(a0.Topla())