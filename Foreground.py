from Globals import *

class Foreground(pygame.sprite.Sprite):
    def __init__(self, filename, layername, sprite_group):
        pygame.sprite.Sprite.__init__(self)
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm
        self.image = self.make_map()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.currentForegroundMap = filename
        sprite_group.add(self)
        camera_sprite.add(self)
    def render(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                if layer.name == "foreground":
                    for x, y, gid, in layer:
                        tile = ti(gid)
                        if tile:
                            surface.blit(tile, (x * self.tmxdata.tilewidth, y * self.tmxdata.tileheight))
    def make_map(self):
        temp_surface = pygame.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface
    def change_map(self, filename, camera):
        #for ent in foreground_layer:
            #ent.kill()
        
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm
        self.image = self.make_map()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.currentMap = filename
        #foreground_layer.add(self)
    def display(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
