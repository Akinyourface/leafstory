from Globals import *
from Pistol import *

class Inventory:
    def __init__(self, player):
        self.player = player
        self.items = []
        self.pistol = Pistol(10, self.player)
        self.items.append(self.pistol)
        self.currentItem = self.items[0]
        self.money = 1000
        self.walletSize = 500
        self.currentMoney = 150
    def draw(self, screen):
        for x in range(len(self.items)):
            screen.blit(self.items[x].image, (x * self.items[x].rect.width, 0))
            #self.pistol.update(dialoguemanager, screen)
    def buy_ammo(self):
        if self.pistol.currentAmmo < self.pistol.maxAmmo and self.money > self.pistol.ammoCost:
            self.pistol.currentAmmo += self.pistol.buyAmmount
            self.currentMoney -= self.pistol.ammoCost
        else:
            print("you have full ammo")
    def get_wallet_size(self):
        return self.walletSize
    def get_money_amount(self):
        return self.currentMoney
    def get_current_item(self):
        return self.currentItem
