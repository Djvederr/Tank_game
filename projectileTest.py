import pygame
import math

# GLOBAL VARIABLES
COLOR = (255, 100, 98)
SURFACE_COLOR = (167, 255, 100)
WIDTH = 800
HEIGHT = 600

# Object class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
            super().__init__()

            self.image = pygame.Surface([width, height])
            self.width=width
            self.color=color
            self.image.fill(SURFACE_COLOR)
            self.image.set_colorkey(COLOR)

            pygame.draw.circle(self.image,color,[width/2, width/2], width/2)

            self.rect = self.image.get_rect()
            self.time=0
            self.startRect=self.image.get_rect()
            print("start : ",self.startRect.x,self.startRect.y)
            
    def update(self):
        angle=math.radians(20)
        speed=100
        if self.rect.y<=580:
            self.time+=0.05
            velx=math.cos(angle)*speed
            vely=math.sin(angle)*speed
            dx=  velx*self.time
            dy=(vely*self.time)+((-9.81*(self.time**2))/2)
            #print(dx,dy)
            self.rect.x=self.startRect.x+dx
            self.rect.y=self.startRect.y-dy
            print(self.rect.x,self.rect.y)
        else:
           self.time=0 
           self.rect.x=self.startRect.x
           self.rect.y=self.startRect.y


pygame.init()

RED = (255, 0, 0)
BLUE = (0,0,255)

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Creating Sprite")

all_sprites_list = pygame.sprite.Group()

object_ = Sprite(RED, 25,25)
object_.rect.x = 10
object_.rect.y = 580
object_.startRect.x = 10
object_.startRect.y = 580


all_sprites_list.add(object_)


exit = True
clock = pygame.time.Clock()
screen.fill(SURFACE_COLOR)
while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
    clock.tick(24)
    all_sprites_list.update()
    all_sprites_list.draw(screen)
    pygame.display.flip()
	

pygame.quit()
