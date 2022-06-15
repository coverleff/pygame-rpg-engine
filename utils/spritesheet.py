import pygame as pg


import json
from sprite.animatedsprite import AnimatedSprite
# Inspired by the pygame wiki's spritesheet class, with some modifications
# to include my format of .json spritesheet meta files

class SpritesheetLoadException(Exception):
    pass

# spritesheet class 
class Spritesheet:
    def __init__(self, spritesheet_filepath : str, meta_filepath : str):
        try:
            self.spritesheet = pg.image.load(spritesheet_filepath).convert()
            self.load_meta(meta_filepath)

        except pg.error as message:
                print('Unable to load spritesheet image:', filepath)
                raise SystemExit(message)

        self.colorkey = self.meta["colorkey"]
        self.cutsize = (self.meta["tile"]["width"], self.meta["tile"]["height"])
        self.animated_images = {}
        self.animated_durations = {}
        
        for anim_name, frames in self.meta["animations"].items():
            tilerects = self.meta["animations"][anim_name]
            rects = [pg.Rect(tilerect[0], tilerect[1], tilerect[2] - tilerect[0], tilerect[3] - tilerect[1]) for tilerect in tilerects]
            # self.animatedsprites[anim_name] = AnimatedSprite(anim_name, self.images_at(rects), self.meta["duration"])
            self.animated_images[anim_name] = self.images_at(rects)
            self.animated_durations[anim_name] = self.meta["duration"]
        
        self.animatedsprite = AnimatedSprite(list(self.animated_images.keys())[0], self.animated_images, self.meta["duration"])
        # (xoffset, yoffset) tuple, size rectangle of each sprites

    # load an image without meta
    def image_at(self, rect):
        image = pg.Surface(rect.size)
        image.blit(self.spritesheet, (0,0), rect)
        if self.colorkey:
            if self.colorkey == -1:
                self.colorkey = image.get_at((0,0))
            image.set_colorkey(self.colorkey, pg.RLEACCEL)
        return image.convert()

    # load list of images without meta
    def images_at(self, rects):
        return [self.image_at(rect) for rect in rects]

    def load_meta(self, filepath):
        with open(filepath, 'r') as f:
            self.meta = json.load(f)

    def get_animatedsprite(self, name):
        return self.animatedsprite
