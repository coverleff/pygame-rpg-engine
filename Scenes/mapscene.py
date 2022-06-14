from Scenes.scene import Scene
# MapScene we will use before we add any cameras, they will then be obsolete
class MapScene(Scene):
    def __init__(self, rendermanager, **kwds):
        super().__init__(self, **kwds)
        self.rendermanager = rendermanager

    def update_map(self):
        self.run_gameobject()
        self.rendermanager.intelligent_draw(self.visible_sprites)
