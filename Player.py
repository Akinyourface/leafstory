from Globals import *
from Gui import *
from Bullet import *

class Player(pygame.sprite.Sprite):
    def __init__(self,startingx, startingy, width, height, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([32, 32])
        self.rect = self.image.get_rect()
        self.image.set_colorkey((0, 0, 0))
        self.rect.x = startingx
        self.rect.y = startingy
        self.velocity = 4
        self.image_left = pygame.image.load('./assets/pirate_left.png')
        self.image_right = pygame.image.load('./assets/pirate_right.png')
        self.deltax = 0
        self.deltay = 0
        self.collidedEntity = False
        self.dir = 0
        self.stamina = 100
        self.isSpaceHeld = False
        self.magic = 100
        self.currentWeapon = "sword"
        self.animationState = "idle"
        self.health = 100
        self.gui = Gui(self)
        self.canMove = True
        player_sprite.add(self)
        camera_sprite.add(self)
    def update_keypressed(self, event, tilemap):        
        #################################
        if self.canMove:
            if event.key == pygame.K_a:
                self.animationState = "walking_left"
                self.deltax = -self.velocity
                self.dir = 1
        #################################   
            elif event.key == pygame.K_d:
                self.animationState = "walking_right"
            
                self.deltax = self.velocity
                self.dir = 2
        #################################    
            elif event.key == pygame.K_w:
            #self.animationState = "walking_left"
                self.deltay = -self.velocity
                self.dir = 3
        #################################    
            elif event.key == pygame.K_s:
            #self.animationState = "walking_right"
                self.deltay = self.velocity
                self.dir = 0
        #################################
            elif event.key == pygame.K_SPACE:
                if(self.gui.inventory.currentItem.name == "simple_pistol"):
                    if(self.gui.inventory.pistol.currentAmmo >= 0):
                   #print("you shot")
                   #print(self.gui.inventory.pistol.currentAmmo)
                        self.gui.inventory.pistol.currentAmmo -= 1
                        bullet = Bullet(self.rect.x, self.rect.y, 16, 16, 10, self.dir)
                        bullet_sprite.add(bullet)
                    else:
                        print("you have no ammo")
            #self.isSpaceHeld = True
            

    def update_keyup(self, event):
        if event.key == pygame.K_a:
            self.deltax = 0
        if event.key == pygame.K_d:
            self.deltax = 0
        if event.key == pygame.K_w:
            self.deltay = 0
        if event.key == pygame.K_s:
            self.deltay = 0
        if event.key == pygame.K_SPACE:
            self.isSpaceHeld = False
    def update(self, background, tiledmap, foreground):
        self.shop_hit = pygame.sprite.spritecollide(self, shopkeeper_sprite, False)
        self.ent_hit = pygame.sprite.spritecollide(self, self.entrance, False)
        for col in self.ent_hit:
            self.change_map(background, tiledmap, foreground,  col.location, col.backgroundMapfile)
        self.rect.x += self.deltax
        self.block_hit = pygame.sprite.spritecollide(self, self.walls, False)
        self.rect.y += self.deltay
        for block in self.block_hit:
            if self.deltax > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
        self.block_hit = pygame.sprite.spritecollide(self, self.walls, False)
        for block in self.block_hit:
            if self.deltay > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
        self.image.fill((0, 0, 0))
        #self.image.set_colorkey((0, 0, 0))
        if self.animationState == "walking_left":
            self.image.blit(self.image_left, (0, 0))
        elif self.animationState == "walking_right":
            self.image.blit(self.image_right,(0, 0))
    def late_update(self):
        pass
    def change_map(self, background, tiledMap, foreground, location, backgroundImage):
        background.change_map(backgroundImage)
        tiledMap.change_map(location, self.camera)
        foreground.change_map(location, self.camera)
    def draw_gui(self, screen, fontrenderer):
        self.gui.draw(screen, fontrenderer)
    def set_previous_entrance(self, entrance):
        self.previous_entrance = entrance
    def set_camera_object(self, object):
        self.camera = object
    def player_died(self):
        self.kill()
        print("You have died, bad luck")
    
