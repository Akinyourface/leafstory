from Globals import *

class Background(pygame.sprite.Sprite):
    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./assets/background.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = (-self.rect.height + SCREEN_HEIGHT) 
        background_layer.add(self)
    def display(self, screen):
        #computational code here
        screen.blit(self.image, (self.rect.x, self.rect.y))
    def change_map(self, backgroundImage):
        self.image = pygame.image.load(backgroundImage)
        
