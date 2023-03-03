import pygame
import random

# GLOBAL VARIABLES
COLOR = (255, 100, 98)
SURFACE_COLOR = (167, 255, 100)
WIDTH = 500
HEIGHT = 500

# Object class
class Sprite(pygame.sprite.Sprite):
	def __init__(self, color, height, width):
		super().__init__()

		self.image = pygame.Surface([width, height])
		self.image.fill(SURFACE_COLOR)
		self.image.set_colorkey(COLOR)

		pygame.draw.rect(self.image,color,pygame.Rect(0, 0, width, height))

		self.rect = self.image.get_rect()
		self.color=color

	def update(self):
		pos=pygame.mouse.get_pos()
		if self.color==RED:
			self.rect=pos




pygame.init()

RED = (255, 0, 0)

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Creating Sprite")

all_sprites_list = pygame.sprite.Group()

object_ = Sprite(RED, 20, 30)
object_.rect.x = 200
object_.rect.y = 300
object2 = Sprite((0,255,0),50,60)
object2.rect.x=400
object2.rect.y=200
all_sprites_list.add(object_)
all_sprites_list.add(object2)

exit = True
clock = pygame.time.Clock()

while exit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit = False

	all_sprites_list.update()
	screen.fill(SURFACE_COLOR)
	all_sprites_list.draw(screen)
	pygame.display.flip()
	clock.tick(60)

pygame.quit()
