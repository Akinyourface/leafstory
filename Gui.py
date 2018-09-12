from Globals import *
from Inventory import *

class Gui(pygame.sprite.Sprite):
    def __init__(self, player):
        self.player = player
        self.inventory = Inventory(self.player)        
        self.inventoryToggle = True
        self.playerImage = pygame.image.load("./assets/pirate_left.png")
        self.playerMoney = pygame.image.load("./assets/money.png")
    def update(self, event):
        pass
    def draw(self, screen, fontrenderer):
        if self.inventoryToggle:
            self.inventory.draw(screen)
        surface = fontrenderer.render(str(self.inventory.pistol.currentAmmo), False, (0, 0, 0))
        health = fontrenderer.render(str(self.player.health), False, (0, 0, 0))
        money = fontrenderer.render(str(self.player.gui.inventory.get_money_amount()), False, (0, 0, 0))
        screen.blit(surface, (45, 0))
        screen.blit(self.playerImage, (SCREEN_WIDTH - 100, 0))
        screen.blit(self.playerMoney, (SCREEN_WIDTH - 100, 50))
        screen.blit(money, (SCREEN_WIDTH - 50, 50))
        screen.blit(health, (SCREEN_WIDTH - 50, 0))
        
