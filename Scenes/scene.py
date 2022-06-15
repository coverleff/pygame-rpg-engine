import pygame as pg
from models.gameobject import GameObject
from models.spriteobject import SpriteObject
import models.collisionobject
from models.collisionobject import CollisionObject
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

        ################################################################
        # Add list of gameobjects with special attributes
        ################################################################

        self.visible_objects = []
        self.collision_objects = []
        self.other_collision_rects = []

    def get_gameobject(self, identifier):
        try:
            return self.gameobjects[identifier]
        except:
            raise UnknownGameObject

    def add_gameobject(self, instance: GameObject):
        if instance.identifier in self.gameobjects.keys():
            raise SameGameObject

        self.gameobjects[instance.identifier] = instance

        ################################################################
        # Add gameobjects with special attributes                      
        # - SpriteObject: objects with a sprite to be rendered
        # - CollisionObject: objects with a collision box
        ################################################################
        if issubclass(type(instance), SpriteObject):
            self.visible_objects.append(instance)

        if issubclass(type(instance), CollisionObject):
            self.collision_objects.append(instance)

    def run_gameobject(self):
        for go in self.gameobjects.values():
            go.update_tick()

    def update(self):
        models.collisionobject.update_collisions(self.collision_objects, self.other_collision_rects)
