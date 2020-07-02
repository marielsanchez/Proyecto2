from vector import Vector

class Plane:

    def __init__(self, material):
        self.distance = float('inf')
        self.position = Vector(0,0,0)
        self.name = "object"
        self.normal = Vector(0,0,1)
        self.material = material

    def intersects(self, ray):
        #for some reason, intersect normal is opposite the light normal. Bug. FIX. Source of bug is light for sure
        inverted = Vector(0,0,0) - self.normal
        denom = ray.direction.dotProduct(inverted)
        #if ray and plane are not very close to perpendicular
        if(denom > 0.000001):
            angle = self.position - ray.position
            t = angle.dotProduct(inverted) / denom
            self.distance = t
            return (t>=0)
        return False
        
    def GetNormal(self, point):
        return self.normal
