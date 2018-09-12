from Globals import *

class Lava(pygame.sprite.Sprite):
    def __init__(self, startingx, startingy, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(startingx, startingy, width, height)
        self.rect.x = startingx
        self.rect.y = startingy
        self.damage = 50
        lava_sprite.add(self)
        camera_sprite.add(self)
    def update(self, player):
        self.player_hit = pygame.sprite.spritecollide(self, player_sprite, False)
        for col in self.player_hit:
            if player.health > 0:
                player.health -= self.damage
            else:
                player.player_died()
