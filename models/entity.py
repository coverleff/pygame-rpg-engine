import pygame as pg
import models.collisionobject
import setup

class Entity(models.collisionobject.CollisionObject, models.spriteobject.SpriteObject):
    
    def __init__(self, position : pg.Vector2, sprite : pg.sprite.Sprite, collision_rect : pg.Rect = pg.Rect(0,0, 16, 10), **kwargs):
        super().__init__(position = position, collision_rect = collision_rect, sprite = sprite, **kwargs)
        self.localcollision_rect.bottom = self.sprite_rect.bottom
        self.localcollision_rect.centerx = self.sprite_rect.centerx

    def update_tick(self):
        super().update_tick()
        #self.blit_collisionbox()
    
    def blit_collisionbox(self):
        collision_surface = pg.Surface(self.collision_rect.size)
        collision_surface.fill(pg.Color(0, 64, 64, 64))
        self.sprite.image.blit(collision_surface, self.localcollision_rect.topleft)

