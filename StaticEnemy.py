from Globals import *
from Fireball import *

class StaticEnemy(pygame.sprite.Sprite):
    def __init__(self, startingx, startingy, image = "./assets/draco_left.png"):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = startingx
        self.rect.y = startingy
        self.name = "static_shooter_enemy"
        self.shooterCounter = 10
        self.dir = 0
        self.defaultLife = 50
        self.currentLife = self.defaultLife
        camera_sprite.add(self)
        skeleton_sprite.add(self)
    def update(self, player):
        if player.rect.x > self.rect.x:
            self.dir = 1
        if player.rect.x < self.rect.x:
            self.dir = 0


        
        if self.currentLife <= 0:
            self.currentLife = self.defaultLife
            #shoot a bullet
            fireball = Fireball(self.rect.x, self.rect.y, "./assets/fireball.png", player)
            fireball_sprite.add(fireball)
        else:
            self.currentLife -= 1
        if self.dir == 0:
            self.image = pygame.image.load("./assets/draco_left.png")
        if self.dir == 1:
            self.image = pygame.image.load("./assets/draco_right.png")
