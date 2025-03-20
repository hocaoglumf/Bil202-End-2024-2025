class Node:
    def __init__(self, val):
        self.sol=None
        self.sag=None
        self.value=val

    def LinkNode(self,node):
        if (self.sol==None):
            self.sol=node
        else:
            self.sag=node

    def AddNested(self):
        left, right=0,0
        if not(self.sol==None):
            left =self.sol.AddNested()
        if not(self.sag==None):
            right=self.sag.AddNested()
        return self.value + left + right

n0=Node(1)
n1=Node(2)
n2=Node(3)
n3=Node(4)
n4=Node(5)

n0.LinkNode(n1)
n0.LinkNode(n2)
n1.LinkNode(n3)
n1.LinkNode(n4)

print(n0.AddNested())

print(n2.AddNested())
