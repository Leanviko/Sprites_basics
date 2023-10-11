import pygame
import sys 

#Classes
class Crosshair(pygame.sprite.Sprite):
    def __init__(self, width, height,pos_x, pos_y, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

# General Setup
pygame.init()
clock = pygame.time.Clock()

#Game Screen
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width,screen_height))

crosshair = Crosshair(50,50,100,100,(255,255,255))

#Create a group 
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    crosshair_group.draw(screen)
    clock.tick(60)