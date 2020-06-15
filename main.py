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

X=700
Y=496


#reference image for background color
im_file = Image.open("img_proyecto2_v2.jpg")
ref = np.array(im_file) #Turns the image into a pixel array

#aux image setup
i = Image.new("RGB", (X, Y), (0, 0, 0) )
px = np.array(i)

screen= pygame.display.set_mode((X,Y))

def getFrame():
    # grabs the current image and returns it
    pixels=np.flip(px,1)
    pixels=np.rot90(pixels,1,(0,1))
    #pixels = np.roll(px,(1,2),(0,1))
    return pixels

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

			
