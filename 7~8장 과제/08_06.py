class Person:
    def __init__(self, name, mobile = "010-0000-0000", office = "000-0000", email = "00000@gmail.com"):
        self.n = name
        self.m = mobile
        self.o = office
        self.e = email
        
    def __str__(self):
        n =str(self.n)
        m =str(self.m)
        o =str(self.o)
        e =str(self.e)
        
        return n, m, o, e
    
    def setName(self, n):
        self.n = n
    def setMobile(self, m):
        self.m = m
    def setOffice(self, o):
        self.o = o
    def setEmail(self, e):
        self.e = e
        
        
        
    def getName(self):
        return self.n
    def getMobile(self):
        return self.m
    def getOffice(self):
        return self.o
    def getEmail(self):
        return self.e
    
    def show(self):
        print(self.n , self.m , self.o , self.e)
        
p1= Person("kim", office = "7894843",email = "kim@company.com")
p2 = Person("Park",office = "1233546")
p2.setEmail("park@ceo.com")
p1.show()
p2.show()
