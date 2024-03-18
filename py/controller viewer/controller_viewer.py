import os
import pygame as pg
import threading
import win32api
import win32con
import win32gui
import ctypes

from method.draw_text import *
from method.img_path import *
from method import nn 


def initialize_pygame():
    pg.init()


def setup_window():
    screen_height = pg.display.Info().current_h
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (80, screen_height - 350)
    screen = pg.display.set_mode((320, 270), pg.NOFRAME)
    return screen


def load_images():
    controller_image_path = pic["controller"]  
    controller_image = pg.image.load(controller_image_path).convert_alpha()

    lt_frame_path = pic["lt_frame"]  
    lt_frame_image = pg.image.load(lt_frame_path).convert_alpha()
    
    rt_frame_path = pic["rt_frame"]  
    rt_frame_image = pg.image.load(rt_frame_path).convert_alpha()

    rb_image = pg.image.load(pic["RB"]).convert_alpha()
    lb_image = pg.image.load(pic["LB"]).convert_alpha()
    
    dd_image = pg.image.load(pic["DD"]).convert_alpha()
    du_image = pg.image.load(pic["DU"]).convert_alpha()
    dl_image = pg.image.load(pic["DL"]).convert_alpha()
    dr_image = pg.image.load(pic["DR"]).convert_alpha()

    return controller_image, lt_frame_image, rt_frame_image, rb_image, lb_image, dd_image, du_image, dl_image, dr_image


def resize_images(controller_image, lt_frame_image, rt_frame_image, rb_image, lb_image, dd_image, du_image, dl_image, dr_image):
    new_width = 300
    new_height = 200

    resized_controller_image = pg.transform.scale(controller_image, (new_width, new_height))
    resized_lt_frame_image = pg.transform.scale(lt_frame_image, (60, 65))
    resized_rt_frame_image = pg.transform.scale(rt_frame_image, (60, 65))

    rb_image = pg.transform.scale(rb_image, (int(139*0.5), int(49*0.5)))
    lb_image = pg.transform.scale(lb_image, (int(139*0.5), int(49*0.5)))
    
    dd_image = pg.transform.scale(dd_image, (int(dd_image.get_width()*0.5), int(dd_image.get_height()*0.5)))
    du_image = pg.transform.scale(du_image, (int(du_image.get_width()*0.5), int(du_image.get_height()*0.5)))
    dl_image = pg.transform.scale(dl_image, (int(dl_image.get_width()*0.5), int(dl_image.get_height()*0.5)))
    dr_image = pg.transform.scale(dr_image, (int(dr_image.get_width()*0.5), int(dr_image.get_height()*0.5)))

    return resized_controller_image, resized_lt_frame_image, resized_rt_frame_image, rb_image, lb_image, dd_image, du_image, dl_image, dr_image


def draw_buttons(screen, joy, resized_controller_image, rb_image, lb_image, dd_image, du_image, dl_image, dr_image):
    button_position = [(239, 151), (239+20, 131), (239-20, 131), (239, 111)]

    button_radius = 11
    if joy.A == 1:
        pg.draw.circle(screen, (250, 250, 250), button_position[0], button_radius)
    if joy.Y == 1:
        pg.draw.circle(screen, (250, 250, 250), button_position[3], button_radius)
    if joy.X == 1:
        pg.draw.circle(screen, (250, 250, 250), button_position[2], button_radius)
    if joy.B == 1:
        pg.draw.circle(screen, (250, 250, 250), button_position[1], button_radius)
    if joy.RightBumper ==1:
        screen.blit(rb_image, (200, 70))
    if joy.LeftBumper ==1:
        screen.blit(lb_image, (50, 70))
    if joy.DownDPad==1:
        screen.blit(dd_image, (116, 172))
    if joy.UpDPad==1:
        screen.blit(du_image, (116, 156))
    if joy.LeftDPad==1:
        screen.blit(dl_image, (100, 172))
    if joy.RightDPad==1:
        screen.blit(dr_image, (116, 172))


def main_thread():
    initialize_pygame()
    screen = setup_window()
    joystick = nn.XboxController()
    clock = pg.time.Clock()
    
    controller_image, lt_frame_image, rt_frame_image, rb_image, lb_image, dd_image, du_image, dl_image, dr_image = load_images()
    resized_controller_image, resized_lt_frame_image, resized_rt_frame_image, rb_image, lb_image, dd_image, du_image, dl_image, dr_image = resize_images(controller_image, lt_frame_image, rt_frame_image, rb_image, lb_image, dd_image, du_image, dl_image, dr_image)
    
    fuchsia = (0, 0, 0)
    hwnd = pg.display.get_wm_info()["window"]
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
    win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
    ctypes.windll.user32.SetForegroundWindow(hwnd)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

        screen.fill(fuchsia)
        screen.blit(resized_controller_image, (10, 70))
        draw_buttons(screen, joystick, resized_controller_image, rb_image, lb_image, dd_image, du_image, dl_image, dr_image)
        
        lt_percentage = joystick.LeftTrigger
        rt_percentage = joystick.RightTrigger
        
        screen.blit(resized_lt_frame_image, (60, 5))
        lt_width = 65 - int(lt_percentage * 65)
        lt_height = min(65, max(0, lt_width)) 
        lt_fill_rect = pg.Rect(60, 5, 60, lt_height)
        screen.blit(resized_lt_frame_image, (60, 5), special_flags=pg.BLEND_RGBA_MULT)
        pg.draw.rect(screen, (0, 0, 0), lt_fill_rect)

        screen.blit(resized_rt_frame_image, (210, 5))
        rt_width = 65 - int(rt_percentage * 65)
        rt_height = min(65, max(0, rt_width)) 
        rt_fill_rect = pg.Rect(210, 5, 60, rt_height)
        screen.blit(resized_rt_frame_image, (210, 5), special_flags=pg.BLEND_RGBA_MULT)
        pg.draw.rect(screen, (0, 0, 0), rt_fill_rect)

        pg.display.flip()
        clock.tick(60)


# 創建後台執行緒
thread = threading.Thread(target=main_thread)
thread.start()
