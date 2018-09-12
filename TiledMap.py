from Globals import *
from Wall import *
from Entrance import *
from Shopkeeper import *
from Skeleton import *
from Lava import *
from Money import *
from StaticEnemy import *
class TiledMap(pygame.sprite.Sprite):
    def __init__(self, filename, player, event, fontrenderer):
        pygame.sprite.Sprite.__init__(self)
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm
        self.player = player
        self.image = self.make_map(self.player, fontrenderer)
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.currentMap = filename
        tiled_layer.add(self)
        self.fontrenderer = fontrenderer
        camera_sprite.add(self)
        self.event = None
        
    def set_event(self, event):
        self.event = event
    def render(self, surface, player):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                if layer.name == "background":
                    for x, y, gid, in layer:
                        tile = ti(gid)
                        if tile:
                            surface.blit(tile, (x * self.tmxdata.tilewidth, y * self.tmxdata.tileheight))
        for object in self.tmxdata.objects:
            if object.name == "player":
                
                
                player.camera.x = object.x
                player.camera.y = object.y
                player.rect.x = object.x
                player.rect.y = object.y
            if object.name == "collidable":
                collidable = Collidable(object.x, object.y, object.width, object.height)
                collision_sprite.add(collidable)
            if object.name == "entrance":
                entrance = Entrance(object.x, object.y, object.width, object.height, object.location, object.backgroundMapfile, player)
            if object.name == "npc":
                if object.type == "shopkeeper":
                    shopkeeper = Shopkeeper(object.x, object.y, self.event, self.fontrenderer)
                    
                    
            if object.name == "musicplayer":
                if object.type == "overworldTheme":
                    pygame.mixer.stop()
                    overworldTheme.play()
                if object.type == "dungeonTheme":
                    pygame.mixer.stop()
                    dungeonTheme.play()
                if object.type == "shopTheme":
                    pygame.mixer.stop()
                    shopTheme.play()
            if object.name == "skeleton":
                skelly = Skeleton(object.x, object.y)
            if object.name == "lava":
                lava = Lava(object.x, object.y, object.width, object.height)
            #add wall code here
            if object.name == "money":
                money = Money(object.x, object.y)
            if object.name == "staticEnemy":
                staticenemy = StaticEnemy(object.x, object.y)
    def make_map(self, player, fontrenderer):
        temp_surface = pygame.Surface((self.width, self.height))
        self.render(temp_surface, player)
        return temp_surface
    def change_map(self, filename, camera):
        #remove all of the objects
        #for ent in tiled_layer:
            #ent.kill()
        
        for ent in entrance_sprite:
            ent.kill()
        for ent in collision_sprite:
            ent.kill()
        for ent in shopkeeper_sprite:
            ent.kill()
        for ent in skeleton_sprite:
            ent.kill()
        for ent in lava_sprite:
            ent.kill()
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm
        self.image = self.make_map(self.player, self.fontrenderer)
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.currentMap = filename
        #tiled_layer.add(self)
    
