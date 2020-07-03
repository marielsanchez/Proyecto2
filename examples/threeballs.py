from color import Color
from light import Light
from material import Material, ChequeredMaterial
from point import Point
from sphere import Sphere
from engine import RenderEngine
from vector import Vector


WIDTH = 960
HEIGHT = 540
RENDERED_IMG = "3balls5.ppm"
CAMERA = Vector(0,-0.35,-1)
OBJECTS = [
    #Ground Plane
    #Aqua color
    Sphere(Point(0, 10000.5, 1),10000.0,
           ChequeredMaterial(
               color1=Color.from_hex("#001326"),
               color2=Color.from_hex("#00172e"),
               ambient = 0.2,
               reflection = 0.2,
               ),
           ),
    
    #Yellow ball
    Sphere(Point(0.0, 0.0, 0.85), 0.6, Material(Color.from_hex("#FCFF2E"))),

    #Pinky ball
    Sphere(Point(1.0, 0.0, 2.0), 0.6, Material(Color.from_hex("#FF6EE2"))),

    #Blue ball
    Sphere(Point(-1.0, 0.0, 2.25), 0.6, Material(Color.from_hex("#002afa"),diffuse = 0.9, specular = 0.2))
    
    ]

LIGHTS = [
    Light(Point(1.5,-0.5,-10), Color.from_hex("#FFFFFF")),
    Light(Point(-0.5,-10.5,0), Color.from_hex("#E6E6E6")),
    ]


