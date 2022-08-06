import pytmx
from Sprite import *


class Map:
     def __init__(self, filename):
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.tilewidth = tm.tilewidth
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm

        self.map_image = pygame.Surface((self.width, self.height)).convert_alpha()
        self.map_rect = self.map_image.get_rect()

        self.all_sprites = pygame.sprite.Group()
        self.objects = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()

        self.render()

     def render(self):
        # self.all_sprites.empty()
        # self.objects.empty()
        # self.walls.empty()
        tile_obj = dict()
        tile_img = dict()
        ti = self.tmxdata.get_tile_image_by_gid
        for tileset in self.tmxdata.tilesets:
            for gid in range(tileset.firstgid, tileset.firstgid + tileset.tilecount):
                tile = ti(gid)
                tile_img[gid] = tile.convert_alpha()

        for gid, colliders in self.tmxdata.get_tile_colliders():  # возвращает все объекты спрайтов
            tile_obj[gid] = colliders

        for group in self.tmxdata.objectgroups:
            print(group)
            if group.name == 'special':
                for obj in group:
                    Obstacle(obj, self.objects)

        print(len(self.objects))

        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if tile:
                        x_pos = x * self.tmxdata.tilewidth
                        y_pos = (y + 1) * self.tmxdata.tileheight - tile.get_size()[1]
                        self.map_image.blit(tile, (x_pos, y_pos))
                        if layer.name == 'objects':
                            print(gid)
                            Wall(tile_img[gid], tile_obj[gid], gid, x_pos, y_pos, self.all_sprites, self.walls)

        print(self.objects)
