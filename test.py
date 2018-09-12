import pygame
from pygame.locals import *

class Actor():
    def __init__(self, startingx, startingy, width, height, image):
        self.startingx = startingx
        self.startingy = startingy
        self.currentX = self.startingx
        self.currentY = self.startingy
        self.width = width
        self.height = height
        self.image = image
    def draw(screen):
        screen.append(self)

class Scrollable():
    def __init__(self):
        cameraSprite.add(self)


class SpriteGroup():
    def __init__(self):
        self.items = []
        
    def add(self,object1):
        self.items.append(object1)
    def draw(self, screen):
        screen.append(self.items)

    def spriteCollide(self, spritegO1, spriteg02):
        pass


class Livable():
    def __init__(self,healthStart, stamina):
        self.health = healthStart
        self.stamina = stamina
        self.isDead = False
    def update(self):
        if self.health <= 0:
            self.isDead = True
        if self.stamina <= 0:
            self.isTired = True
    def mmotest(self):
        print(str(self.health))
        
class Player(Collidable, Scrollable, Livable):
    def __init__(self, startingx, startingy, image):
        Collidable.__init__(self, startingx, startingy, 16, 16, image)
        Scrollable.__init__(self)
        Livable.__init__(self, 100, 100)
        self.deltax = 0
        self.deltay = 0
    def update_keypressed(self,event):
        pass

    def update_keypressed_up(self,event):
        pass
    def update(self):
        pass
    
cameraSprite = SpriteGroup()
playerSprite = SpriteGroup()

player = Player(10, 10, "./assets/player.png")
playerSprite.add(player)

