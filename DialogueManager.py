from Globals import *

class DialogueManager(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.showablex = 10
        self.showabley = 10
        self.default_font = pygame.font.SysFont('Comic Sans MS', 30)
        self.fontscreen = self.default_font.render("This is a test", False, (0, 0, 0))
        self.rendererableobjects = []
    def draw(self, surface, screen, x, y):
        #screen.blit(surface,(x, y))
        pass
