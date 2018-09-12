from Globals import *

class Pistol(pygame.sprite.Sprite):
    def __init__(self,damage,  player):
        pygame.sprite.Sprite.__init__(self)
        self.damage = damage
        self.image = pygame.image.load("./assets/pistol.png")
        self.rect = self.image.get_rect()
        
        self.name = "simple_pistol"
        self.player = player
        self.ammoCost = 15
        self.buyAmmount = 1
        camera_sprite.add(self)
        self.maxAmmo = 15
        self.currentAmmo = self.maxAmmo
        self.dir = self.player.dir
    def render_text(self):
        #rendertext = dialoguemanager.default_font.render(str(self.currentAmmo), False, (0, 0, 0))
        pass
    def update(self):
        #self.render_text(dialoguemanager, screen)
        pass
