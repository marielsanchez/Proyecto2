class Image:
    width = 1
    height = 1
    #pixels = [[]]

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [[None for _ in range(width)]for _ in range(height)]
        
    def set_pixel(self, x, y, col):
        #normally its x,y but y,x its convencional 
        self.pixels[y][x] = col
        
    def write_ppm(self, img_file):
        def to_byte(c):
            #max and min make the number be between 0 and 255 values
            return round(max(min(c * 255,255),0))

        img_file.write("P3 {} {}\n255\n".format(self.width,self.height))
        for row in self.pixels:
            for color in row:
                img_file.write(
                    "{} {} {} ".format(
                        to_byte(color.x), to_byte(color.y), to_byte(color.z)
                        )
                    )
            img_file.write("\n")     





        
