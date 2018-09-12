from Globals import *

class MainMenu:
    def __init__(self, gsm):
        self.currentOption = 0
        self.options = []
        self.font = "placeholder"
        self.options.append("Start Game")
        self.options.append("Credits")
        self.menuscreen = pygame.image.load("./assets/mainmenu.png")
        self.player = pygame.image.load("./assets/pirate_left.png")
        self.gsm = gsm
        self.menux = 30
        self.menuy = 210
    def update(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and self.currentOption >= 0 + 1:
                self.currentOption -= 1
            if event.key == pygame.K_s and self.currentOption != len(self.options) - 1:
                self.currentOption += 1
            if event.key == pygame.K_RETURN:
                if self.currentOption == 0:
                    self.gsm.set_state("s_main_game")
                if self.currentOption == 1:
                    self.gsm.set_state("s_credits")
        #print(self.options[self.currentOption])
        #print(str(self.currentOption))
    def draw(self, screen):
        screen.fill((0, 0, 0))
        screen.blit(self.menuscreen, (0, 0))
        if(self.currentOption == 0):
            screen.blit(self.player, (55, 210))
        elif(self.currentOption == 1):
            screen.blit(self.player, (55, 265))
        pygame.display.flip()
