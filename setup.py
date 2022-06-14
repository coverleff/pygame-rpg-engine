import pygame as pg


class Setup:
    clock = None
    _instance = None
    def __init__(self):
        if Setup._instance is None:
            Setup._instance = self
        else:
            raise ValueError("Two Setup instances... Quit")
        pg.init()
        self.size = (720, 480)
        self.screen = pg.display.set_mode(self.size, pg.RESIZABLE) 
        pg.display.set_caption("testmap")

        self.screen.fill((255, 255, 255))
        pg.display.flip()

        self.clock = pg.time.Clock()
        Setup.clock = self.clock

        self.fps = 100

        rect = pg.Rect((0, 0), (32, 32))
        image = pg.Surface((32, 32))
        pg.draw.rect(self.screen, (255,0,0), (400, 400, 20, 20),0)
        pg.display.update()

