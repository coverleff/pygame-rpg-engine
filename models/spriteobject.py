from models.gameobject import GameObject
import pygame as pg
from sprite.animatedsprite import AnimatedSprite
import models.localposition

class SpriteObject(GameObject):
    def __init__(self, position: pg.Vector2, sprite: pg.sprite.Sprite, layer=0, identifier=None, **kwargs):
        super().__init__(position, identifier=identifier, **kwargs)
        self.sprite = sprite
        self.sprite_rect = models.localposition.LocalRect(sprite.rect, localsys = self.localsys)
        self.layer = layer

    def update_tick(self):
        super().update_tick()
        self.sprite.update()

    @property
    def image(self):
        return self.sprite.image

