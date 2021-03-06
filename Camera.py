from Globals import *

class Camera:
    def __init__(self, player):
        self.player = player
        self.offset = 16 * 16
        self.x = 0
        self.y = 0
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    def update(self, background, tiledmap, foregroundmap):
        #############################################
        if self.player.rect.x < (0 + self.offset):
            if(tiledmap.rect.x < 0) and (foregroundmap.rect.x < 0) and (background.rect.x <= 0):
                #print(str(background.rect.x))
                for ent in camera_sprite:
                    ent.rect.x += 4
                for ent in background_layer:
                    ent.rect.x += 1
                
            self.rect.x += 4
            
        #############################################            
        if self.player.rect.x > (self.width - self.offset):
            if((tiledmap.rect.x + tiledmap.rect.width) > self.rect.width) and ((foregroundmap.rect.x + foregroundmap.rect.width) > self.rect.width) and ((background.rect.x + background.rect.width) > self.rect.width):
                self.rect.x += 4
                for ent in camera_sprite:
                    ent.rect.x -= 4
                for ent in background_layer:
                    ent.rect.x -= 1
            self.rect.x -= 4
        #############################################
        if self.player.rect.y < (0 + self.offset):
            if (tiledmap.rect.y < 0) and (foregroundmap.rect.y < 0):
                for ent in camera_sprite:
                    ent.rect.y += 4
            self.rect.y += 4
        #############################################        
        if self.player.rect.y > (self.height - self.offset):
            if((tiledmap.rect.y + tiledmap.rect.height) > self.rect.height) and ((foregroundmap.rect.y + foregroundmap.rect.height) > self.rect.height):
                for ent in camera_sprite:
                    ent.rect.y -= 4
            self.rect.y -= 4
        ############################################
