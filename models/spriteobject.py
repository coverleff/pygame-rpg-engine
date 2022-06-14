from models.gameobject import GameObject
import pygame as pg
from sprite.animatedsprite import AnimatedSprite

class SpriteObject(GameObject):
    def __init__(self, position: pg.Vector2, sprite: pg.sprite.Sprite, identifier=None):
        super().__init__(position, identifier=identifier)
        self.sprite = sprite
        self.rect = pg.Rect(position, sprite.rect.size)
        self.sprite.rect = self.rect

    def update_tick(self):
        super().update_tick()
        self.sprite.update()


    @property
    def image(self):
        return self.sprite.image


