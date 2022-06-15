from setup import Setup
from Scenes import MapScene
import pygame as pg
from rendermap import MapRenderManager
import utils.path, utils.spritesheet
import models.spriteobject
import models.player
import sys
from Scenes.mapmanager import MapManager

class Main:

    def __init__(self, *args, **kwargs):
        self.setup = Setup()
        manager = MapManager('testmap.tmx')
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

            
            self.Scene.run_gameobject()
            self.Scene.update()
            self.Scene.update_map()
            self.debug_run()

    def test(self):
        sheet = utils.spritesheet.Spritesheet("ressources/spritesheets/spritesheet_zelda.png", "ressources/spritesheets/spritesheet_zelda.json")
        self.go = models.player.Player(position = pg.Vector2(50, 10), sprite = sheet.animatedsprite)
        self.Scene.add_gameobject(self.go)

        sheet2 = utils.spritesheet.Spritesheet("ressources/spritesheets/spritesheet_zelda.png", "ressources/spritesheets/spritesheet_zelda.json")
        self.go2 = models.player.Player(position = pg.Vector2(50, 50), sprite = sheet2.animatedsprite, movable=False)
        self.Scene.add_gameobject(self.go2)


    def debug_run(self):
        pass

if __name__ == "__main__":
    instance = Main()
    instance.run()
