from models.gameobject import GameObject
from models.localposition import LocalRect
import pygame as pg
from Scenes.mapmanager import MapManager
from Scenes.mapscene import MapScene
class Camera(GameObject):
    instances = []
    current = None

    def __init__(self, mapscene : MapScene, _frame_rect : pg.Rect = None):

        self.mapmanager = mapscene.mapmanager
        self.pixel_size = self.mapmanager.pixel_size 

        
        if _frame_rect is None:
            _frame_rect = pg.Rect((0,0), self.pixel_size)
        
        super().__init__(_frame_rect.topleft)
        
        self.frame_rect = LocalRect((0,0), _frame_rect.size, localsys = self.localsys)

        Camera.instances.append(self)
        self.scene = mapscene
        
        if Camera.current is None:
            Camera.current = self
            self.active = True
        
        else:
            self.active = False
        self.blit_surface = self.mapmanager.blit_surface

    def update_tick(self):
        if not self.active:
            return

        self.blit_surface(self.scene.screen, self.scene.visible_objects)
        pg.display.update()

    def isactive(self):
        return self.active

    def setactive(self):
        Camera.current.active = False
        Camera.current = self
        self.active = True
