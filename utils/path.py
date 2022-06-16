import config

def get_spritesheet(name):
    return '/'.join(config.SPRITESHEETS.split('/') + [name + ".png"]), '/'.join(config.SPRITESHEETS.split('/')+ [name + ".json"])
def get_map(name):
    return '/'.join(config.MAPS.split('/') + [name + ".tmx"])
