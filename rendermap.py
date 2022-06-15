import pygame as pg
import pytmx
import models

'''
This will be replaced by a camera game object that will process map tiles and stuff before returning something a pg.Surface to display
'''

class MapRenderManager:
    def __init__(self, map_path, screen):
        tiled_map = pytmx.util_pygame.load_pygame(map_path)
        self.pixel_size = tiled_map.width * tiled_map.tilewidth, tiled_map.height * tiled_map.tileheight
        self.tiled_map_data = tiled_map
        self.screen = screen

        th = self.tiled_map_data.tileheight
        tw = self.tiled_map_data.tilewidth
        
        self.tiles = []
        self.colliders = []
        for i, layer in enumerate(self.tiled_map_data.visible_layers):
            for x, y, image in layer.tiles():
                z = tiled_map.get_tile_properties(x, y, i)['z']
                self.tiles.append((x*tw,y*th, (i + z)*th + y*th, image))
                
                properties = tiled_map.get_tile_properties(x, y, i)
                if "colliders" in properties.keys():
                    colliders = properties["colliders"]
                    self.colliders += [pg.Rect(c.x, c.y, c.width, c.height) for c in colliders]


        self.tiles.sort(key=lambda t: t[2])
    

    def render_map(self, surface):
        if self.tiled_map_data.background_color:
            surface.fill(pg.Color(self.tiled_map_data.background_color))

        for layer in self.tiled_map_data.visible_layers:
            self.render_tile_layer(surface, layer)

    def render_tile_layer(self, surface, layer):
        tw = self.tiled_map_data.tilewidth
        th = self.tiled_map_data.tileheight
        surface_blit = surface.blit

        for x, y, image in layer.tiles():
            surface_blit(image, (x*tw, y*th))

    def draw(self, spritegroup):
        screen = self.screen
        temp = pg.Surface(self.pixel_size)
        
        self.render_map(temp)
        self.drawsprites(temp, spritegroup = spritegroup)

        pg.transform.smoothscale(temp, screen.get_size(), screen)
        pg.display.flip()

    def drawsprites(self, surface, spritegroup = None):
        if spritegroup is not None:
            spritegroup.draw(surface)
    
    def intelligent_draw(self, spriteobjects : list[models.spriteobject.SpriteObject]):
        # We will make a list with the tiles and the sprite and sort them by z_visible value.
        # For sprites, the z_visible would correspond to rect.bottom, to which we add the layer they are at.
        # For tiles, we need to get their metadatas z and add the layer they are at.
        # For time gaining purposes, the list of tiles will be presorted and the sprites will be appended on the right order in the render_tile list
        
        th = self.tiled_map_data.tileheight
        tw = self.tiled_map_data.tilewidth
        
        screen = self.screen
        surface = pg.Surface(self.pixel_size)

        new_images = self.tiles[:]
        
        for gameobj in spriteobjects:
            sprite_rect = gameobj.sprite_rect.globalrect()
            new_images.append((sprite_rect.left, sprite_rect.top, sprite_rect.bottom + gameobj.layer * th, gameobj.sprite.image))
        new_images.sort(key = lambda t: t[2])
        surface_blit = surface.blit
        for x, y, z, img in new_images:
            surface_blit(img, (x, y))

        pg.transform.smoothscale(surface, screen.get_size(), screen)
        pg.display.flip()
