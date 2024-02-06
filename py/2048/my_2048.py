import pygame as pg
from method import *
pg.init() 
screen_width = 500
screen_height = 500
screen = pg.display.set_mode((screen_width, screen_height))
screen_size={"width":screen_width,"hight":screen_height}
screen.fill(color.good_look_blue)
main.run(screen)