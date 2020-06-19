import random
import numpy as np
from Point import *
from PIL import Image
import rt
import math
import threading
import pygame 
import sys

pygame.init()

#Constants
PI=math.pi
#Colors
WHITE=(255,255,255)
BLACK=(0,0,0)
GREEN=(0,255,0)
RED=(255,0,0)
BORDER=50

WIDTH=600
HEIGHT=600

def raytrace():
    #Raytraces the scene progessively
    while True:
        #random point in the image
        point = Point(random.uniform(0, 600), random.uniform(0, 600))
        #pixel color
        pixel = 0
        for source in sources:
            #calculates direction to light source
            
            dir = source-point
            #add jitter
            #dir.x += random.uniform(0, 25)
            #dir.y += random.uniform(0, 25)

            #distance between point and light source
            length = rt.length(dir)
            #normalized distance to source
            length2 = rt.length(rt.normalize(dir))
            
            

            #colorBleeding = False
            #if seg in colorSegments:
            #        colorBleeding = True
            
            #checks if the light gets there
            free = True
            for seg in segments:                
                #check if ray intersects with segment
                dist = rt.raySegmentIntersect(point, dir, seg[0], seg[1])
                #if intersection, or if intersection is closer than light source
                if  dist > 0 and length2>dist:
                    free = False
                    break

            if free:        
                intensity = (1-(length/500))**2
                #print(len)
                #intensity = max(0, min(intensity, 255))
                values = (ref[int(point.y)][int(point.x)])[:3]
                #combine color, light source and light color
                values = values * intensity * light
                
                #add all light sources 
                pixel += values
                
            
            #average pixel value and assign
            px[int(point.x)][int(point.y)] = pixel // len(sources)

#reference image for background color
im_file = Image.open("img_proyecto2_v6.jpg")
ref = np.array(im_file) #Turns the image into a pixel array

#light positions
sources = [ Point(257,442), Point(493,175) ]

light = np.array([1, 1, 0.75])

#aux image setup
i = Image.new("RGB", (WIDTH, HEIGHT), (0, 0, 0) )
px = np.array(i)

screen= pygame.display.set_mode((WIDTH,HEIGHT))

#warning, point order affects intersection test!!
segments = [
            ([Point(6,56), Point(128,56)]),#Square 
            ([Point(126,56), Point(126,154)]),
            ([Point(126,152), Point(6,152)]),
            ([Point(8,152), Point(8,56)]),
            ([Point(33,323), Point(117,243)]),#Triangle
            ([Point(115,243), Point(115,347)]),
            ([Point(33,323), Point(8,56)]),
            ([Point(249,129), Point(348,73)]),#Rhomboid
            ([Point(348,73), Point(430,137)]),
            ([Point(430,137), Point(323,177)]),
            ([Point(323,177), Point(249,132)]),
            ([Point(417,75), Point(501,7)]),#Green Triangle
            ([Point(501,7), Point(541,117)]),
            ([Point(417,75), Point(541,117)]),
            ([Point(440,492),Point(503,369)]),#Red Triangle
            ([Point(503,369), Point(581,475)]),
            ([Point(581,475), Point(440,492)]),
            ([Point(70,442), Point(149,415)]),#Pentagon
            ([Point(149,415), Point(230,496)]),
            ([Point(230,496), Point(136,554)]),
            ([Point(136,552), Point(21,507)]),
            ([Point(21,507), Point(73,442)])
            ]

colorSegments = [
            ([Point(417,75), Point(501,7)]),#Green Triangle
            ([Point(501,7), Point(541,117)]),
            ([Point(417,75), Point(541,117)]),
            ([Point(440,492),Point(503,369)]),#Red Triangle
            ([Point(503,369), Point(581,475)]),
            ([Point(581,475), Point(440,492)]),
            ([Point(70,442), Point(149,415)]),#Pentagon
            ([Point(149,415), Point(230,496)]),
            ([Point(230,496), Point(136,554)]),
            ([Point(136,552), Point(21,507)]),
            ([Point(21,507), Point(73,442)])
            ]


def getFrame():
    # grabs the current image and returns it
    #pixels=np.flip(px,1)
    #pixels=np.rot90(pixels,1,(0,1))
    pixels = np.roll(px,(1,2),(0,1))
    return pixels

#thread setup
t = threading.Thread(target = raytrace) # f being the function that tells how the ball should move
t.setDaemon(True) # Alternatively, you can use "t.daemon = True"
t.start()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Clear screen to white before drawing 
    screen.fill((255, 255, 255))

    # Get a numpy array to display from the simulation
    npimage=getFrame()

    # Convert to a surface and splat onto screen offset by border width and height
    surface = pygame.surfarray.make_surface(npimage)
    screen.blit(surface, (0, 0))
    pygame.display.flip()

			
