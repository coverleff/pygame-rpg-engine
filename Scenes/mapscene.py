from Scenes.scene import Scene
from Scenes.mapmanager import MapManager
import pygame as pg

class MapScene(Scene):
    def __init__(self, mapmanager : MapManager, screen, **kwds):
        super().__init__(self, **kwds)
        self.mapmanager = mapmanager
        self.screen = screen
        self.other_collision_rects += mapmanager.get_rect_colliders()
        
    def update(self):
        super().update()
