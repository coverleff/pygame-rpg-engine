from models.gameobject import GameObject
import pygame as pg
from models.localposition import LocalRect

class CollisionObject(GameObject):
    " Collision game object, has a localcollision_rect and collision_rect, and stop fonctionnalities"

    def __init__(self, position, collision_rect : pg.Rect, identifier=None, stop_on_collision=True, movable=True, **kwargs):
        super().__init__(position, identifier = identifier, **kwargs)
        self.localcollision_rect = LocalRect(collision_rect.topleft, collision_rect.size, localsys = self.localsys)
        self.stop_on_collision = stop_on_collision
        self.movable = movable

    def on_collision(self, collide_rect : pg.Rect):
        if self.stop_on_collision:
            if self.movable and self.collision_rect.colliderect(collide_rect):
                self._stop(collide_rect)

    @property
    def collision_rect(self):
        return self.localcollision_rect.globalrect()


    def _stop(self, collide_rect : pg.Rect, collide_range = 12):
        rec1 = collide_rect
        rec2 = self.localcollision_rect.globalrect()
        
        
        dx1 = rec1.right - rec2.left
        dx2 = rec2.right - rec1.left
        dy1 = rec1.bottom - rec2.top
        dy2 = rec2.bottom - rec1.top

        if dx2 < collide_range < dx1:
            self.localsys.x -= dx2
            
        elif dx1 < collide_range < dx2:
            self.localsys.x += dx1
        
        if dy2 < collide_range < dy1:
            self.localsys.y -= dy2
        
        elif dy1 < collide_range < dy2:
            self.localsys.y += dy1

# TODO
# This can be improved from N**2 to NlogN with a sophisticated algorithm
def update_collisions(collisionobjects : list[CollisionObject], static_collision_rects : list[pg.Rect]):
    collision_rects = [cgo.collision_rect for cgo in collisionobjects]
    for i, cgo in enumerate(collisionobjects):
        colliding = cgo.collision_rect.collidelistall(collision_rects[i+1:])
        for index in colliding:
            collisionobjects[index+i+1].on_collision(cgo.collision_rect)
            cgo.on_collision(collisionobjects[index+i+1].collision_rect)

        colliding = cgo.collision_rect.collidelistall(static_collision_rects)
        for index in colliding:
            cgo.on_collision(static_collision_rects[index])
