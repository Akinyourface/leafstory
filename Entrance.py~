from Globals import *

class Entrance(pygame.sprite.Sprite):
    def __init__(self, startingx, startingy, width, height, location, backgroundMapfile, player):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height= height
        self.rect = pygame.Rect(startingx, startingy, self.width, self.height)
        self.location = location
        self.backgroundMapfile = backgroundMapfile
        camera_sprite.add(self)
        entrance_sprite.add(self)
