from setup import Setup
from Scenes import MapScene
import pygame as pg
from rendermap import MapRenderManager
import utils.path, utils.spritesheet
import models.spriteobject
import sys
class Main:

    def __init__(self, *args, **kwargs):
        self.setup = Setup()
        render = MapRenderManager("testno.tmx", self.setup.screen)
        self.Scene = MapScene(render)
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
                self.go.move((0,-2))
            elif keys[pg.K_DOWN]:
                self.go.move((0,2))
            elif keys[pg.K_RIGHT]:
                self.go.move((2,0))
            elif keys[pg.K_LEFT]:
                self.go.move((-2,0))
            elif keys[pg.K_q]:
                sys.exit()


            self.Scene.update_map()

    def test(self):
        sheet = utils.spritesheet.Spritesheet("ressources/spritesheets/spritesheet_zelda.png", "ressources/spritesheets/spritesheet_zelda.json")
        self.go = models.spriteobject.SpriteObject(pg.Vector2(10, 10), sheet.animatedsprites["walk_down"])
        self.Scene.add_gameobject(self.go)

    def debug_run(self):
        pass


if __name__ == "__main__":
    instance = Main()
    instance.run()
