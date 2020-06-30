from point import Point

class Square:
    """
    2D shape implemented.
    """
    def __init__(self, pointA, pointB, pointC, pointD, material):
        self.pointA = pointA
        self.pointB = pointB
        self.pointC = pointC
        self.pointD = pointD
        self.material = material  


    def intersects(self, ray):
        """
        Checks if the ray intersects any of the
        segments of the square. It should intersects in two
        points of the square so it returns the nearest point of
        intersection to the ray or None if theres no intersection
        """
        def raySegmentIntersectAB(self, ray):
            """
            recibes a ray. checks if it intersects the segment
            dot: denominator. if dot = 0 they're paralel
            t1: distance from origin to intersection
            t2: intersection IN the segment
            """
            v1 = ray.origin - self.pointA
            v2 = self.pointB - self.pointA
            v3 = Point(ray.direction.y, ray.direction.x, 0)
            dot = v2.dot(v3)
            if (abs(dot) < 0.000001):
                return None
            t1 = v2.cross(v1) / dot
            t2 = v1.dot(v3) / dot
            if (t1 >= 0.0 and (t2 >= 0.0 and t2 <= 1.0)):
                return t1
            return None
        
        def raySegmentIntersectCD(self, ray):
            v1 = ray.origin - self.pointC
            v2 = self.pointD - self.pointC
            v3 = Point(ray.direction.y, ray.direction.x,0)
            dot = v2.dot(v3)
            if (abs(dot) < 0.000001):
                return None
            t1 = v2.cross(v1) / dot
            t2 = v1.dot(v3) / dot
            if (t1 >= 0.0 and (t2 >= 0.0 and t2 <= 1.0)):
                return t1
            return None
        
        def raySegmentIntersectAC(self, ray):
            v1 = ray.origin - self.pointA
            v2 = self.pointC - self.pointA
            v3 = Point(ray.direction.y, ray.direction.x,0)
            dot = v2.dot(v3)
            if (abs(dot) < 0.000001):
                return None
            t1 = v2.cross(v1) / dot
            t2 = v1.dot(v3) / dot
            if (t1 >= 0.0 and (t2 >= 0.0 and t2 <= 1.0)):
                return t1
            return None

        def raySegmentIntersectBD(self, ray):
            v1 = ray.origin - self.pointB
            v2 = self.pointD - self.pointB
            v3 = Point(ray.direction.y, ray.direction.x,0)
            dot = v2.dot(v3)
            if (abs(dot) < 0.000001):
                return None
            t1 = v2.cross(v1) / dot
            t2 = v1.dot(v3) / dot
            if (t1 >= 0.0 and (t2 >= 0.0 and t2 <= 1.0)):
                return t1
            return None
        
        minD = 9999
        distance_AB = raySegmentIntersectAB(self, ray)
        distance_CD = raySegmentIntersectCD(self, ray)
        distance_AC = raySegmentIntersectAC(self, ray)
        distance_BD = raySegmentIntersectBD(self, ray)
        
        if distance_AB is not None:
            minD = distance_AB
        if distance_CD is not None:
            if distance_CD < minD:
                minD = distance_CD
        if distance_AC is not None:
            if distance_AC < minD:
                minD = distance_AC
        if distance_BD is not None:
            if distance_BD < minD:
                minD = distance_BD

        if minD != 9999:
            return minD
        return None
    
    

        
