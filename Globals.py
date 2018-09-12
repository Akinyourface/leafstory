import pygame
from pygame.locals import *
import pytmx

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FPS = 60
pygame.init()
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.font.init()
background_layer = pygame.sprite.Group()
tiled_layer = pygame.sprite.Group()
foreground_layer = pygame.sprite.Group()

camera_sprite = pygame.sprite.Group()
player_sprite = pygame.sprite.Group()
wall_sprite = pygame.sprite.Group()
collision_sprite = pygame.sprite.Group()
entrance_sprite = pygame.sprite.Group()
gui_sprite = pygame.sprite.Group()
bullet_sprite = pygame.sprite.Group()
shopkeeper_sprite = pygame.sprite.Group()
skeleton_sprite = pygame.sprite.Group()
lava_sprite = pygame.sprite.Group()
money_sprite = pygame.sprite.Group()
shopmenu_sprite = pygame.sprite.Group()
fireball_sprite = pygame.sprite.Group()
currentTrack = ""
overworldTheme = pygame.mixer.Sound("./assets/music/littletown.ogg")
dungeonTheme = pygame.mixer.Sound("./assets/music/dungeon.ogg")
shopTheme = pygame.mixer.Sound("./assets/music/buysomething.ogg")
#shopTheme.play()
class Actor(pygame.sprite.Sprite):
    def __init__(self, startingx, startingy, width, height, filename):
        pygame.sprite.Sprite.__init__(self)
        print("in the actor class")
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.x = startingx
        self.rect.y = startingy

