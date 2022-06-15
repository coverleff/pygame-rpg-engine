import pygame as pg
import config
import setup
class AnimatedSprite(pg.sprite.Sprite):
    def __init__(self, init_animation : str, animation_dict : dict[str,list[pg.surface.Surface]], duration: float, loop = True, layer = 0):
        super().__init__()
        self.animation_dict = animation_dict
        self.current_animation = init_animation
        self.images = animation_dict[init_animation]
        self.duration = duration
        self.loop = loop
        self.index = 0
        self.max_index = len(self.images)
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

    def change_animation(self, new_animation, start_index=0):
        if new_animation == self.current_animation:
            return

        self.images = self.animation_dict[new_animation]
        self.current_animation = new_animation
        self.image = self.images[start_index]
        self.max_index = len(self.images)

    def set_animation_index(self, index):
        self.index = index
