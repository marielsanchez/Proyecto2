class Vector:
    x = 0.0
    y = 0.0
    z = 0.0

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "({},{},{})".format(self.x,self.y,self.z)
    
    def __magnitude__(self):
        #gets the distance from the origin to a particular vector
        result = self.x**2 + self.y**2 + self.z**2
        return result**(1/2)

    def __dotProduct__(self, vector2):
        #returns de dotProduct between 2 vectors
        return self.x * vecto2.x + self.y * vector2.y + self.z * vector2.z

    def __normalize__(self):
        magnitude = __magnitude__(self)
        if magnitude == 0:
            return
        else:
            return self/magnitude

    def __addition__(self, vector2):
        #returns de dotProduct between 2 vectors
        return Vector(self.x + vecto2.x, self.y + vector2.y, self.z + vector2.z)

    def __subtraction__(self, vector2):
        #returns de dotProduct between 2 vectors
        return Vector(self.x - vecto2.x, self.y - vector2.y, self.z - vector2.z)
    
    def __multiply__(self, n):
        #returns de dotProduct between 2 vectors
        assert not isinstance(n, Vector)
        return Vector(self.x * n, self.y * n, self.z *n)

    def __rMul__(self, vector2):
        return self.__rMul__(vector2)
    

    def __division__(self, n):
        #returns de dotProduct between 2 vectors
        assert not isinstance(n, Vector)
        return Vector(self.x / n, self.y / n, self.z /n)



    
