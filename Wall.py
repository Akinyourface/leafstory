from Globals import *

class Collidable(pygame.sprite.Sprite):
    def __init__(self, startingx, startingy, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.x = startingx
        self.y = startingy
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        camera_sprite.add(self)
        collision_sprite.add(self)
