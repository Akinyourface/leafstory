from Globals import *
from random import randint

class npc(pygame.sprite.Sprite):
    def __init__(self, startingx, startingy, width, height, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = startingx
        self.rect.y = startingy
        self.dir = 0 #left 1: right
        self.deltax = 0
        self.deltay = 0
        self.dialogue = []
        camera_sprite.add(self)
