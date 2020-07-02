from color import Color

class Light:
    """
    Represents a point of a light source of a certain color
    """
    def __init__(self, position, color = Color.from_hex("#FFFFFF")):
        #take ou the Color if you want a light from a diferent color
        self.position = position
        self. color = color
