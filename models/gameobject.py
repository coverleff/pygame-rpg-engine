import uuid
import pygame as pg
import models.localposition
import Scenes.scene

class GameObject:
    def __init__(self, position, identifier=None, **kwargs):
        if not identifier:
            identifier = str(uuid.uuid4())
        
        self.identifier = identifier
        self.localsys = models.localposition.LocalSystem(position)

    '''
    Run this method every tick
    '''
    def update_tick(self):
        pass

    def move(self, movement: pg.Vector2):
        self.coordinates = self.coordinates + movement

    @property
    def coordinates(self):
        return self.localsys

    @coordinates.setter
    def coordinates(self, position : pg.Vector2):
        self.localsys.xy = position
