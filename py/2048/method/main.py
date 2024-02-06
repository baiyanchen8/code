import pygame as pg
from . import keyboard as kb
from . import color
from . import map
import keyboard
def run(screen):
    running=True
    kbc=kb.kbcontroller()
    keyboard.hook(kbc.lka)
    clock=pg.time.Clock()
    while(running):
        clock.tick_busy_loop(60)
        # quit event
        screen.fill(color.good_look_blue)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        kbc.mapping.draw(screen)
        pg.display.flip()
    pg.quit()