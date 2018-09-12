from Globals import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, startingx, startingy, width, height, velocity, dir):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./assets/bullet.png")
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = startingx
        self.rect.y = startingy
        self.dir = dir
        self.velocity = velocity
        self.life = 100
    def update(self):
        if self.life > 0:
            self.life -= 1
        else:
            self.kill()

        if(self.dir == 2):
            self.velocity = 10
        elif(self.dir == 1):
            self.velocity = -10
        self.rect.x += self.velocity
        
        
