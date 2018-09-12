from Globals import *
import math

class Fireball(pygame.sprite.Sprite):
    def __init__(self, startingx, startingy, image, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = startingx
        self.rect.y = startingy
        self.rotation = math.atan2(player.rect.y - self.rect.y, player.rect.x - self.rect.x)
        self.speed = 2
        self.deltax = 0
        self.deltay = 0
        self.damage = 5
        camera_sprite.add(self)
        self.life = 500
        self.defaultLife = 500
        #very crude way of extracting data from the player object
        
    def update(self, player):
        #self.dx, self.dy = self.rect.x - player.rect.x, self.rect.y - player.rect.y
        #self.dist = math.hypot(self.dx, self.dy)
        self.collision = pygame.sprite.spritecollide(self, player_sprite, False)
        for col in self.collision:
            if player.health > 0:
                player.health -= self.damage
                self.kill()
            else:
                player.player_died()
        if self.life >= 0:
            self.rect.x += math.cos(self.rotation) * self.speed
            self.rect.y += math.sin(self.rotation) * self.speed
            self.life -= 1
        else:
            self.kill()
        
