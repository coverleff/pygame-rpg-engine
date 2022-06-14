import pygame as pg
import config
import setup
class AnimatedSprite(pg.sprite.Sprite):
    def __init__(self, animation_name : str, frame_images : list[pg.surface.Surface], duration: float, loop = True, layer = 0):
        super().__init__()
        self.name = animation_name
        self.images = frame_images
        self.duration = duration
        self.loop = loop
        self.index = 0
        self.max_index = len(frame_images)
        self.image = self.images[self.index]
        self.rect = pg.Rect((0,0), self.image.get_size())
        self.last_tick = pg.time.get_ticks()
        # used in the order of rendering objects
        self.layer = layer

    def update(self):
        if pg.time.get_ticks() - self.last_tick > self.duration:
            
            if self.loop:
                self.index = (self.index+1) % self.max_index
            else:
                self.index = min(self.index, self.max_index)
            
            self.image = self.images[self.index]
            #self.rect.width, self.rect.height = self.image.get_size()
            self.last_tick = pg.time.get_ticks()

