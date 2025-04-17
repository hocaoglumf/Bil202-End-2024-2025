class MyNode:
    def __init__(self):
        self._value=0
        self.__children=[]

    def Attach(self, dugum):
        self.__children.append(dugum)

    def GetValue(self):
        return self._value

    def SetValue(self,v):
        self._value=v

    def GetChildrenValue(self):
        list=[]
        for i in self.__children:
            list.append(i.GetValue())
        return list

n0=MyNode()
n1=MyNode()
n2=MyNode()
n3=MyNode()
n4=MyNode()
n5=MyNode()
n6=MyNode()

n0.SetValue(3)
n1.SetValue(5)
n2.SetValue(6)
n3.SetValue(7)
n4.SetValue(1)
n6.SetValue(9)

n0.Attach(n1)
n0.Attach(n2)
n0.Attach(n3)

n1.Attach(n4)
n1.Attach(n5)
n2.Attach(n6)

h=n0.GetChildrenValue()
print(h)





