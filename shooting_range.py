import pygame
import sys
import random


#Classes
class Crosshair(pygame.sprite.Sprite):
    def __init__(self,picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path) 
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound("gunshot.mp3")
    def shoot(self):
        #self.gunshot.set_volume(0.5)
        self.gunshot.play()
        self.gunshot.set_volume(0.02)
        pygame.sprite.spritecollide(crosshair, target_group,True)
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.image = pygame.transform.scale(self.image,(60,60)) 
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

# General Setup
pygame.init()
clock = pygame.time.Clock()

#Game Screen
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))
background = pygame.image.load("BG.png")
pygame.mouse.set_visible(False) #Mouse pointer is not visible



#Create a group of crosshair
crosshair = Crosshair("crosshair.png")
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

#Target
target_group = pygame.sprite.Group()
for target in range(10):
    new_target = Target("target.png", random.randrange(0,screen_width), random.randrange(0,screen_height))
    target_group.add(new_target)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()

    pygame.display.flip()
    screen.blit(background,(0,0))
    target_group.draw(screen)

    crosshair_group.draw(screen)
    crosshair_group.update()
    clock.tick(60)