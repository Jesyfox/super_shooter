__author__ = 'Bogdan.S'
import sys
import pygame as pg
import Objects.GameObject as gobj
pg.init()

size = width, height = (640, 480)
black = (0, 0, 0)

screen = pg.display.set_mode(size)
screen.fill(black)

player = pg.image.load('player.jpg').convert()
resize = [int(i/6) for i in player.get_rect() if i]
player = pg.transform.scale(player, resize)

objects = []

for i in range(10):
    o = gobj.GameObject(player, i*40, i)
    objects.append(o)


def main():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

        for o in objects:
            o.move()
            screen.blit(o.image, o.rect)

        pg.display.update()
        pg.time.delay(100)
        screen.fill(black)


if __name__ == '__main__':
    main()
