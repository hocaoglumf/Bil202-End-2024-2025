
class Student:
    def __init__(self):
        self.name=""
        self.surname=""
        self.no=""

    def Write(self):
        print(self.name,"  ",self.surname,"  ",self.no)

class Class:
    def __init__(self,name):
        self.name=name
        self.students=[]

    def Register(self,s):
        self.students.append(s)

    def ClassList(self):
        for i in self.students:
            print(i.name," ", i.surname, " ", i.no)

    def ChangeNumber(self,cond,add):
        for i in self.students:
            if i.no[0]==cond:
                i.no +=add

end1=Class("Endüstri 1")
s0=Student()
s1=Student()
s2=Student()
s3=Student()
s0.name="Ali"
s0.surname="Uzun"
s0.no="234234"

s1.name="Veli"
s1.surname="Kısa"
s1.no="4353234"

s2.name="Ahmet"
s2.surname="Kara"
s2.no="546456"

s3.name="Mehmet"
s3.surname="Beyaz"
s3.no="09099"

end1.Register(s0)
end1.Register(s1)
end1.Register(s2)
end1.Register(s3)
end1.ClassList()
end1.ChangeNumber("5","*")
end1.ClassList()



