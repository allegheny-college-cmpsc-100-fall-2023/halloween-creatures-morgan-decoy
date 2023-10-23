from vpython import * #import vpython library
from models import * #import models.py file, allowing us to use those functions

scene.range = 6
scene.background = vector(126/255, 128/255, 178/255)

#draw glowing moon in corner
moon = sphere(pos = vector(5, 4, 0), radius = 1, color = color.white, emissive = True, emissiveColor = color.yellow)

#function that draws different halloween creature depending on mouse position
def clickFunc():
    if scene.mouse.pos.y > 0:   
        black_cat(scene.mouse.pos, 1)

# while loop that runs continuously   
while True: 
    rate(30) #rate of 30 frames per second
    #binds mouseup event to clickFunc, so that when you release mouse clickFunc happens
    scene.bind('mouseup', clickFunc)



   