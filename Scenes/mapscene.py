from Scenes.scene import Scene
from Scenes.mapmanager import MapManager
import pygame as pg

class MapScene(Scene):
    def __init__(self, mapmanager : MapManager, screen, **kwds):
        super().__init__(self, **kwds)
        self.mapmanager = mapmanager
        self.screen = screen

        self.other_collision_rects += mapmanager.get_rect_colliders()
        #self.rendermanager = rendermanager
        
    def update_map(self):
        self.run_gameobject()
        self.mapmanager.blit_surface(self.screen, self.visible_objects)

        pg.display.flip()
        #self.rendermanager.intelligent_draw(self.visible_objects)
