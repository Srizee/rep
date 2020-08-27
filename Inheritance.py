class  Person:
    def __init__(self,name):
        self.name = name

    def getName(self):
        return self.name


class Student(Person):
    def __init__(self,name,batch):
        super().__init__(name)
        self.batch = batch
        
    def getBatch(self):
        return self.batch



s = Student("Ram","CSIT")
print(s.getName())
print(s.getBatch())