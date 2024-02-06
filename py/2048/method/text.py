import pygame as pg
def draw_text(screen,text,size,x,y,color):
    font = pg.font.Font(None, size)
    str1=str(text)
    score_text = font.render(str1, True, color)
    screen.blit(score_text, (x+(40-len(str1)*10), y+40))