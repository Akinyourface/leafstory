from Globals import *

class Money(pygame.sprite.Sprite):
    def __init__(self, startingx, startingy, image = "./assets/money.png"):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = startingx
        self.rect.y = startingy
        self.worth = 5
        money_sprite.add(self)
        camera_sprite.add(self)

    def update(self, player):
        self.col_sprite = pygame.sprite.spritecollide(self, player_sprite, False)
        for col in self.col_sprite:
            if player.gui.inventory.get_money_amount() < player.gui.inventory.get_wallet_size():
                player.gui.inventory.currentMoney += self.worth
                self.kill()
