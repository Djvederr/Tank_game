import pygame as py  

# define constants  
WIDTH = 500  
HEIGHT = 500  
FPS = 30  

# define colors  
BLACK = (0 , 0 , 0)
WHITE=(255,255,255)
GREEN = (0 , 255 , 0)  

# initialize pygame and create screen  
py.init()  
screen = py.display.set_mode((WIDTH , HEIGHT))
clock = py.time.Clock()  
rot = 0 
rot_speed = 2
# for setting FPS
image_orig = py.Surface((20 , 100))  
# for making transparent background while rotating an image  
image_orig.set_colorkey(BLACK)
image_orig.fill(GREEN)
running = True
rect = image_orig.get_rect()
rect.x = 100
rect.y = 100
rot = (rot + rot_speed) % 360
while rot<90:  
    # set FPS  
    clock.tick(FPS)  
    # clear the screen every time before drawing new objects  
    screen.fill(WHITE)
    for event in py.event.get():  
        if event.type == py.QUIT:  
            running = False
    #rot = (rot + rot_speed) % 360
    rot=45
    print(rot)
    #rot=120
    # rotating the orignal image  
    new_image = py.transform.rotate(image_orig , rot)  
    rect2 = new_image.get_rect()
    
    rect2.x=rect.x +100
    rect2.y=rect.y +100
    #print(rect2)
    screen.blit(image_orig , rect)
    screen.blit(new_image , rect2)
    py.display.flip()  
#py.quit()
