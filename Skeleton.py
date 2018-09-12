from Globals import *
import math

class Skeleton(pygame.sprite.Sprite):
    def __init__(self, startingx, startingy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./assets/skeleton.png")
        self.rect = self.image.get_rect()
        self.rect.x = startingx
        self.rect.y = startingy
        self.dir = 0
        self.deltax = 0
        self.deltay = 0
        self.health = 100
        self.damage = 15
        self.speed = -3
        self.health = 100
        skeleton_sprite.add(self)
        camera_sprite.add(self)
    def update(self, player):
        #fix a divide by zero crash on the following code
        if self.health > 0:
            self.bullet_col = pygame.sprite.spritecollide(self, bullet_sprite, False)
            for col in self.bullet_col:
                self.health -= player.gui.inventory.get_current_item().damage
                col.kill()
            self.dx, self.dy = self.rect.x - player.rect.x, self.rect.y - player.rect.y
            self.dist = math.hypot(self.dx, self.dy)
            self.dx, self.dy = self.dx / self.dist, self.dy / self.dist
            self.deltax = player.rect.x / self.rect.x
            self.deltay = player.rect.y / self.rect.y
        
            if self.dist < 200:
                self.rect.x += self.dx * self.speed
                self.block = pygame.sprite.spritecollide(self, collision_sprite, False)
                self.rect.y += self.dy * self.speed
                for block in self.block:
                    if self.dx * self.speed  > 0:
                        self.rect.right = block.rect.left
                    else:
                        self.rect.left = block.rect.right
                self.block = pygame.sprite.spritecollide(self, collision_sprite, False)
                for block in self.block:
                    if self.dy * self.speed > 0:
                        self.rect.bottom = block.rect.top
                    else:
                        self.rect.top = block.rect.bottom
        else:
            self.kill()
