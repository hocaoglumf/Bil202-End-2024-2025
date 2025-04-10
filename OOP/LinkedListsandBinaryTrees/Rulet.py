import random

class Slot:
    def __init__(self):
        self.value=random.randint(0,100)
        self.next=None

    def Turn(self):
        return self.next

class Board:
    def __init__(self):
        self.Wheele=[]
        self.pointer=None

    def Add(self,slt):
        uz=len(self.Wheele)
        if uz>0:
            self.Wheele[uz-1].next=slt
        self.Wheele.append(slt)
        self.pointer=self.Wheele[0]

    def Finalize(self):
        uz=len(self.Wheele)
        self.Wheele[uz-1].next=self.Wheele[0]

    def Turn(self):
        self.pointer=self.pointer.Turn()


board=Board()
for i in range(10):
    board.Add(Slot())

board.Finalize()

turnNum=random.randint(10,100)
for i in range(turnNum):
    print("--->",board.pointer.value)
    board.Turn()

print("::",board.pointer.value)

