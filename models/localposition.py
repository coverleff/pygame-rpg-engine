import pygame as pg

class LocalSystem(pg.Vector2):
    def __init__(self, position : pg.Vector2):
        super().__init__(position)
        " position: parent's position"
    
    @property
    def coordinates(self):
        return self

    def localtoglobalcoordinates(self, localcoordinates : pg.Vector2):
        return self + localcoordinates

class LocalRect(pg.Rect):
    def __init__(self, *args, localsys : LocalSystem, **kwargs):
        self.localsys = localsys
        super().__init__(*args, **kwargs)

    def globalrect(self):
        return pg.Rect(self.localsys.localtoglobalcoordinates(self.topleft), self.size)
    
    # TODO: globalrect setter
