from Globals import *

class ShopMenu(pygame.sprite.Sprite):
    def __init__(self, startingx, startingy, fontrenderer):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./assets/shopBackgroundimage.png")
        self.rect = self.image.get_rect()
        self.rect.x = startingx
        self.rect.y = startingy
        self.options = []
    
        self.renderedOption = []
        self.options.append("Pistol Ammo")
        self.currentOption = 0
        self.show = False
        for element in player_sprite:
            self.options.append("Bag Upgrade " + " Wallet Size: " + str(element.gui.inventory.walletSize))

        self.options.append("Exit Menu")
        self.render(fontrenderer)
        shopmenu_sprite.add(self)
        
    def update(self, player, event, fontrenderer):
        if self.show:
            player.canMove = False
            if event.type == pygame.KEYDOWN:
                if event.key == K_w:
                    if self.currentOption >= 0 + 1:
                        self.currentOption -= 1
                if event.key == K_s:
                    if self.currentOption < len(self.options) - 1:
                        self.currentOption += 1
                if event.key == pygame.K_SPACE:
                    if self.currentOption == 0:
                        player.gui.inventory.buy_ammo()
                    if self.currentOption == 1:
                        print("test")
                    if self.currentOption == 2:
                        self.show = False
                        player.canMove = True
            self.draw()
    def render(self, fontrenderer):
        for option in range(len(self.options)):
            renderedOption = fontrenderer.render(self.options[option], False, (0, 0, 0))
            self.renderedOption.append(renderedOption)
            print("rendererd")
            #for option in range(len(self.options)):
            #    for element in range(len(self.renderedOptions)):
            #        self.image.blit(self.renderedOptions[element], (self.rect.width / 2, self.rect.height / 2 * option))
            #for element in range(len(self.renderedOption)):
                #self.image.blit(self.renderedOption[element], (self.rect.width / 2 * element, self.rect.height / 2))
    def draw(self):
        for element in range(len(self.renderedOption)):
            self.image.blit(self.renderedOption[element], (self.rect.width / 2, (self.rect.height / 2) + 20* element))
        
        
        
