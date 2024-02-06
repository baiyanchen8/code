import pygame as pg

def draw_text(screen, font_path, text, size, x, y, color):
    if font_path:
        font = pg.font.Font(font_path, size)
    else:
        font = pg.font.Font(None, size)

    text_surface = font.render(str(text), True, color)
    screen.blit(text_surface, (x, y))