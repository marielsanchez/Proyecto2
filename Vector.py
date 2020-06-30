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
    
    def magnitude(self):
        #gets the distance from the origin to a particular vector
        result = self.x**2 + self.y**2 + self.z**2
        return result**(1/2)

    def dotProduct(self, vector2):
        #returns de dotProduct between 2 vectors
        return self.x * vector2.x + self.y * vector2.y + self.z * vector2.z

    def normalize(self):
        magnitude = self.magnitude()
        if magnitude == 0:
            return
        else:
            return self/magnitude

    def __add__(self, vector2):
        #returns de dotProduct between 2 vectors
        return Vector(self.x + vector2.x, self.y + vector2.y, self.z + vector2.z)

    def __sub__(self, vector2):
        #returns de dotProduct between 2 vectors
        return Vector(self.x - vector2.x, self.y - vector2.y, self.z - vector2.z)
    
    def __mul__(self, n):
        #returns de dotProduct between 2 vectors
        assert not isinstance(n, Vector)
        return Vector(self.x * n, self.y * n, self.z *n)

    def __rmul__(self, vector2):
        return self.__mul__(vector2)
    
    def __truediv__(self, n):
        #returns de dotProduct between 2 vectors
        assert not isinstance(n, Vector)
        return Vector(self.x / n, self.y / n, self.z /n)

    def dot(self, p2):
        return (self.x*p2.x) + (self.y*p2.y)

    def cross(self, p2):
        return (self.x*p2.y) - (self.y*p2.x)



    
