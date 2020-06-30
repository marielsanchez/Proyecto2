class Ray:
    """
    Half line with an origin and a direction
    """
    def __init__(self,origin,direction):
        self.origin = origin
        self.direction = direction.normalize()
        
        
