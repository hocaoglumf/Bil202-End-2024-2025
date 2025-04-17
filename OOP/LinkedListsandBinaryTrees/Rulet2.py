import random

class Slot:
    def __init__(self,value):
        self.value=value
        self.next=None

    def Turn(self):
        return self.next

class Board:
    def __init__(self,slotNumber):
        self.Wheele=[]
        self.pointer=None
        self.__valueList=self.ValueList(slotNumber)
        self.CreateSlots(slotNumber)

    def CreateSlots(self,nmbr):
        for i in range(nmbr):
            val=self.__valueList[0]
            s=Slot(val)
            self.__valueList.remove(val)
            self.Add(s)
        self.Finalize()
        start=random.randint(0,len(self.Wheele)-1)
        self.pointer = self.Wheele[start]


    def ValueList(self, sltNum):
        liste = []
        while True:
            x = random.randint(0, 100)
            if not (x in liste):
                liste.append(x)
            if len(liste) >= sltNum:
                break
        return liste

    def Add(self,slt):
        uz=len(self.Wheele)
        if uz>0:
            self.Wheele[uz-1].next=slt
        self.Wheele.append(slt)


    def Finalize(self):
        uz=len(self.Wheele)
        self.Wheele[uz-1].next=self.Wheele[0]

    def Turn(self):
        self.pointer=self.pointer.Turn()


board=Board(10)


turnNum=random.randint(10,100)
for i in range(turnNum):
    print("--->",board.pointer.value)
    board.Turn()

print("::",board.pointer.value)

