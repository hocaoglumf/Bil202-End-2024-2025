class Node:
    def __init__(self):
        self.sol=None
        self.sag=None

    def LinkNode(self,node):
        if (self.sol==None):
            self.sol=node
        else:
            self.sag=node
n0=Node()
n1=Node()
n2=Node()
n3=Node()
n4=Node()



n0.LinkNode(n1)
n0.LinkNode(n2)
n1.LinkNode(n3)
n1.LinkNode(n4)