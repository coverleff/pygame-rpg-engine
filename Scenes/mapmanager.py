import pygame as pg
from pygame import Rect
import pytmx

class MapManager:
    def __init__(self, filepath):
        self.tiled_map = tiled_map = pytmx.load_pygame(filepath)
        self.pixel_size = tiled_map.width * tiled_map.tilewidth, tiled_map.height * tiled_map.tileheight
        
        self.th = th = tiled_map.tileheight
        self.tw = tw = tiled_map.tilewidth
        
        # For rendering purposes, every visible tile will be here...
        # format : (x, y, layer)

        self.tiles = []
        self.tiles_properties = {}
        for i, layer in enumerate(tiled_map.visible_layers):
            for x, y, image in layer.tiles():
                # Tile z axis for rendering purposes
                self.tiles_properties[(x,y,i)] = tiled_map.get_tile_properties(x, y, i)
                z = tiled_map.get_tile_properties(x, y, i)['z']
                self.tiles.append( (x * tw, y * th, (i + z + y) * th, image) )

        self.colliding_tiles = self.get_rect_colliders()

    def get_rect_colliders(self):
        rects = []
        for coords, prop in self.tiles_properties.items():
            if "colliders" in prop.keys():
                colliders = prop["colliders"]
                rects += [pg.Rect( coords[0] * self.tw + c.x, coords[1] * self.th + c.y, c.width, c.height ) for c in colliders]
                for c in colliders:
                    print(coords, self.tw, self.th, c.x, c.y)
                    print(pg.Rect( coords[0] * self.tw + c.x, coords[1] * self.th + c.y, c.width, c.height ))

        return rects

    def blit_surface(self, surface : pg.Surface, gameobjects):
        " From a rect, blit in on a surface and return it "
        tw, th = self.th, self.tw
        real_surface = pg.Surface(self.pixel_size)

        new_tile_images = self.tiles[:]

        for go in gameobjects:
            sprite_rect = go.sprite_rect.globalrect()
            new_tile_images.append((sprite_rect.x, sprite_rect.y, sprite_rect.bottom + go.layer * th, go.sprite.image))
        
        new_tile_images.sort(key=lambda t: t[2])
        surface_blit = real_surface.blit

        for x, y, z, img in new_tile_images:
            surface_blit(img, (x, y))

        # Resize the real image to the screen...
        pg.transform.smoothscale(real_surface, surface.get_size(), surface)
