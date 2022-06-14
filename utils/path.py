import config

def get_spritesheet(name):
    return '/'.join([config.SPRITESHEETS.strip('/'), name + ".png"])

