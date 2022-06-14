import pygame as pg
from models.gameobject import GameObject
class UnknownGameObject(Exception):
    pass
class SameGameObject(Exception):
    pass

class Scene(object):
    scene_instances = []

    def __init__(self, name=None):
        self.name = name
        Scene.scene_instances.append(self)
        self.gameobjects = {}
        self.visible_sprites = pg.sprite.RenderPlain()

    def get_gameobject(self, identifier):
        try:
            return self.gameobjects[identifier]
        except:
            raise UnknownGameObject

    def add_gameobject(self, instance: GameObject):
        if instance.identifier in self.gameobjects.keys():
            raise SameGameObject
        
        self.gameobjects[instance.identifier] = instance



        if hasattr(instance, "sprite"):
            self.visible_sprites.add(instance.sprite)

    def run_gameobject(self):
        for go in self.gameobjects.values():
            go.update_tick()
