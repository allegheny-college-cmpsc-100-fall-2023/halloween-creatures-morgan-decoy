from vpython import *

#define function that draws a black cat
def black_cat(pos, scale):
   #img src: https://www.istockphoto.com/vector/symbolic-cute-cat-face-gm1204008191-346275524
   head = sphere(texture = 'catface.jpg', pos = pos, scale = vector(scale, scale, scale), color = color.white) #draws head and wraps with catface image
   ear1 = pyramid(pos = pos + vector(-0.4*scale, 0.45*scale, -0.25), scale = vector(0.5*scale, 0.5*scale, 0.5*scale), color = color.black) #draws left ear
   ear2 = pyramid( pos = pos + vector(0.25*scale, 0.25*scale, 0), scale = vector(0.5*scale, 0.5*scale, 0.5*scale), color = color.black) #draws right ear
   ear2.rotate(angle = radians(45), axis = vector(0, 0, 1)) #rotates right ear

#define function that draws a pumpkin
def pumpkin(pos):
   #img src: https://pva.supply/product/minecraft-jack-o-lantern/
   p = sphere(pos = pos)  #main pumpkin with jack-o-lantern texture
   p.texture = 'Minecraft-Jack-O-Lantern.jpg' #assign texture to pumpkin
   cylinder(pos = pos + vector(0, 1, 0), radius = 0.2, axis = vector(0, 1, 0), color = color.green) #stem