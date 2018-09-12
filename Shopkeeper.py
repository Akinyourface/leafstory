from Globals import *
from NPC import *
from random import randint
from ShopMenu import *
class Shopkeeper(npc):
    def __init__(self, startingx, startingy, event, fontrenderer):
        super().__init__(startingx, startingy, 32, 32, "./assets/shopkeeper_right.png")
        self.dialogue.append("Welcome to my shop, please buy something")
        self.dialogue.append("I owe childsupport, please buy something")
        self.dialogue.append("Be careful in the caves, you're my only customer!")
        self.dialogue.append("Press space to buy more ammo for your pistol")
        self.dialogue.append("Please tell your friends about us...if you do have friends")
        self.dialogue.append("I'm watching you buddy...")
        self.event = event
        shopkeeper_sprite.add(self)
        self.player = player_sprite
        self.saidOption = randint(0,len(self.dialogue) - 1)
        self.renderText = True
        self.shopMenu = ShopMenu(0, 0, fontrenderer)
    def update(self, player, fontrenderer):
        self.hit_list = pygame.sprite.spritecollide(self, self.player, False)
        for col in self.hit_list:
            if self.event.type == pygame.KEYDOWN:
                if self.event.key == pygame.K_SPACE:
                    self.shopMenu.show = True
        if player.rect.x > self.rect.x:
            self.dir = 1
        if player.rect.x < self.rect.x:
            self.dir = 0
            
        if self.dir == 0:
            self.image = pygame.image.load("./assets/shopkeeper_left.png")
        if self.dir == 1:
            self.image = pygame.image.load("./assets/shopkeeper_right.png")
        self.shopMenu.update(player, self.event, fontrenderer)
    def render_text(self, screen, fontrenderer, camera):
        if self.renderText == True:
            rendererd = fontrenderer.render(self.dialogue[self.saidOption], False, (0, 0, 0))
            screen.blit(rendererd, (self.rect.x - len(self.dialogue[self.saidOption]) * 2, self.rect.y - 250))
    def set_event(self, event):
        self.event = event
