import pygame as pg
import time
import json
import random

''' ugly code that does the job of generating metadata for spritesheets'''
colors = pg.colordict.THECOLORS
name = input("Input spritesheet name (without .json): ")
pg.init()

img = pg.image.load(name+".png")

rect = img.get_rect()
screen = pg.display.set_mode(rect.size)

screen.fill(pg.colordict.THECOLORS["yellow1"])
screen.blit(img, (0,0))

print("size: {}".format(rect.size))

while True:
    if pg.event.poll().type == pg.QUIT:
        break

    pg.display.flip()


'''
find tile size, well kinda
'''
sprect = None
run = True
while run:
    tilesize = list(map(int, input("Input tile size in px separated by a space: ").split()))
    sprect = pg.Rect(0,0,tilesize[0], tilesize[1])
    pg.draw.rect(screen, pg.colordict.THECOLORS["yellow1"], sprect)
    pg.display.flip()
    run = 'y' in input("wrong size? type y: ")
    screen.blit(img, (0,0))
    pg.display.flip()


'''
Image notations, make animations...
'''

animations = {}

pg.font.init()
font = pg.font.SysFont(None, sprect.size[0]//2)
run = True
sprite_rects = []
ignore_rects = []

# It was a while but too lazy to change
if run:
    print("gen animations")
    for x in range(rect.size[0]//sprect.size[0]):
        for y in range(rect.size[1]//sprect.size[1]):
            if (x,y) in ignore_rects:
                continue
            sprite_rects.append(pg.Rect(x*sprect.size[0], y*sprect.size[1], sprect.size[0], sprect.size[1]))
    
    print(sprite_rects)
    '''
    Disco rects!
    '''
    for r in sprite_rects:
        pg.draw.rect(screen, random.choice(list(colors.values())), r)
    pg.display.flip()
    input()
    screen.fill(pg.colordict.THECOLORS["yellow1"])
    screen.blit(img, (0,0))
    pg.display.flip()

    '''
    Show the coordinates
    '''
    for r in sprite_rects:
        textsurface = font.render(','.join([str(r.x), str(r.y)]), True, colors["black"])
        screen.blit(textsurface, (r.x, r.y))
        pg.display.flip()


    while True:
        anim_name = input("new animation name: ")
        
        if not anim_name:
            break

        anim_sprite_rects = []
        while True:
            coords = input("Input tile coord in px separated by a space: ")
            if not coords:
                break

            x,y = list(map(int, coords.split()))
            for r in sprite_rects:
                if r.x == x and r.y == y:
                    print("found rect {}".format(r))
                    coords = r
                    break
            else:
                print("incorrect tile coord, input new anim tile in {}...".format(anim_name))
                continue

            anim_sprite_rects.append((coords.left, coords.top, coords.right, coords.bottom))
            print("appended to anim " + anim_name+ " !" )
        
        print(anim_sprite_rects)
        animations[anim_name] = anim_sprite_rects 

dico = {
        "spritesheet": {"height" : rect.y, "width": rect.x},
        "tile": {"height" : tilesize[1], "width": tilesize[0]},
        "colorkey": -1,
        }

dico["animations"] = animations
dumped = json.dumps(dico, indent=4)
with open(name+".json", 'w') as f:
    f.write(dumped)


