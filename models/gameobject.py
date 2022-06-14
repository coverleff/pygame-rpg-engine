import uuid
import pygame as pg
class GameObject:
    def __init__(self, position, identifier=None):
        self.rect = pg.Rect(position, (0, 0))
        if not identifier:
            identifier = str(uuid.uuid4())
        
        self.identifier = identifier

    '''
    Run this method every tick
    '''
    def update_tick(self):
        pass

    def move(self, movement: pg.Vector2):
        self.rect.move_ip(movement)

