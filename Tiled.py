from Globals import *
class TiledMap(pygame.sprite.Sprite):
    def __init__(self, filename, player):
        pygame.sprite.Sprite.__init__(self)
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm
        self.player = player
        self.image = self.make_map(self.player)
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.currentMap = filename
        tiled_layer.add(self)
    def render(self, surface, player):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layer:
            if isinstance(layer, pytmx.TiledTileLayer):
                if layer.name is not "foreground":
                    for x, y, gid, in layer:
                        tile = ti(gid)
                        if tile:
                            surface.blit(tile, (x * self.tmxdata.tilewidth, y * self.tmxdata.tileheight))
        for object in self.tmxdata.objects:
            if object.name == "player":
                player.rect.x = object.x
                player.rect.y = object.y
            #add wall code here
    def make_map(self, player):
        temp_surface = pygame.Surface((self.width, self.height))
        self.render(temp_surface, player)
        return temp_surface
    def change_map(self, filename):
        #remove all of the objects
        for ent in tiled_layer:
            ent.kill()
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm
        self.image = self.make_map(self.player)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.currentMap = filename
        tiled_layer.add(self)
    
