class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        
    def __str__(self):
        x = str(self.x)
        y = str(self.y)
        w = str(self.width)
        h = str(self.height)
        
        return x, y, w, h

    
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def getW(self):
        return self.__w
    def getH(self):
        return self.__h
    
    def setX(self,x):
        self.__x = x
    def setY(self,y):
        self.__y = y
    def setW(self,w):
        self.__w = w
    def setH(self,h):
        self.__h = h
        

    def getArea(self):
        print("넓이는 ", self.width *self.height)
        
    def overlap(self, r):
        if (self.x < r.x <(self.x+self.width)) or (self.x < (r.x + r.width) <(self.x+self.width)):
            print("r1과 r2는 서로 겹칩니다.")
        elif (self.y < r.y < (self.y-self.height)) or (self.y < (r.y - r.height) < (self.y-self.height)):
            print("r1과 r2는 서로 겹칩니다.")
        else:
            print("r1과 r2는 서로 겹치지 않습니다.")
        
r1 = Rectangle(0,0,100,100)
r2 = Rectangle(10,10,100,100)
r1.overlap(r2)
r1.getArea()
        
        
    
    
    
        #Coordinates = "사각형의 좌표 : " + str(self.x) +","+ str(self.y)
        #Size = "사각형의 크기: " + str(self.width)+ "x" + str(self.height)
        #return Coordinates
        #return Size
    