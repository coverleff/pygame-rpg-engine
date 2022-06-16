from setup import Setup
from Scenes import MapScene
import pygame as pg
from rendermap import MapRenderManager
import utils.path, utils.spritesheet
import models.spriteobject
import models.entity
import sys
from Scenes.mapmanager import MapManager
import models.camera
class Main:

    def __init__(self, *args, **kwargs):
        self.setup = Setup()
        manager = MapManager(utils.path.get_map('testmap'))
        self.Scene = MapScene(manager, self.setup.screen)
        self.clock = self.setup.clock
        self.test()
        self.run()

    def run(self):
        running = True
        fps = self.setup.fps

        while running:
            self.clock.tick_busy_loop(fps)
            pg.display.set_caption(f'playground - {int(self.clock.get_fps())}fps')
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            keys = pg.key.get_pressed()
            if keys[pg.K_UP]:
                self.go.move((0,-6))
                self.go.sprite.change_animation("walk_up")
            elif keys[pg.K_DOWN]:
                self.go.move((0,6))
                self.go.sprite.change_animation("walk_down")
            elif keys[pg.K_RIGHT]:
                self.go.move((6,0))
                self.go.sprite.change_animation("walk_right")
            elif keys[pg.K_LEFT]:
                self.go.move((-6,0))
                self.go.sprite.change_animation("walk_left")
            elif keys[pg.K_q]:
                sys.exit()

            elif keys[pg.K_0]:
                print(self.go.sprite_rect.globalrect())
                print(self.go.collision_rect)

            
            self.Scene.update()
            self.debug_run()

    def test(self):
        print('uh')
        print(utils.path.get_spritesheet("Characters/Character 1"))
        sheet = utils.spritesheet.Spritesheet(*utils.path.get_spritesheet("Characters/Character 1"))
        self.go = models.entity.Entity(position = pg.Vector2(50, 10), sprite = sheet.animatedsprite)
        self.Scene.add_gameobject(self.go)

        sheet2 = utils.spritesheet.Spritesheet(*utils.path.get_spritesheet("Characters/Character 1"))
        self.go2 = models.entity.Entity(position = pg.Vector2(50, 50), sprite = sheet2.animatedsprite, movable=False)
        
        self.Scene.add_gameobject(self.go2)
        self.Scene.add_gameobject(models.camera.Camera(self.Scene))
    def debug_run(self):
        pass

if __name__ == "__main__":
    instance = Main()
    instance.run()
