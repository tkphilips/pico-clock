
import interstate75
import time

from clock import Clock
from progress import ProgressBar
from colour import White, Green
from message import ScrollMessage

DISPLAY_TYPE = interstate75.DISPLAY_INTERSTATE75_64X32

i75 = interstate75.Interstate75(display=DISPLAY_TYPE)
graphics = i75.display

#WHITE = graphics.create_pen(255, 255, 255)
#WHITE = graphics.create_pen_hsv(1.0, 0.0, 0.5)
BLACK = graphics.create_pen(0, 0, 0)
WHITE = Green(graphics)

def draw_clock(graphics, clock):
    print('draw', clock.time)
    graphics.set_font('bitmap8')
    #graphics.set_pen(WHITE)
    WHITE.use()
    graphics.text(clock.time, 0, 1, scale=2)

def draw_date(graphics, clock):
    print('draw', clock.date)
    graphics.set_font('bitmap4')
    #graphics.set_pen(WHITE)
    WHITE.use()
    graphics.text(clock.date, 10, 24, scale=1)

def clear_screen(graphics):
    graphics.set_pen(BLACK)
    graphics.clear()
    

def run_clock():
    pbar = ProgressBar(2, 16, 60, 0, 59)
    brightness = 0.0
    sm = ScrollMessage()
    
    while True:
        if i75.switch_pressed(interstate75.SWITCH_A):
            sm.print(i75, graphics, 'button a')
            continue
        
        brightness += 0.01
        clock = Clock()
        pbar.set_progress(clock.dt.second)
        WHITE.set_brightness(brightness)
        print('brightness', brightness)
        
        clear_screen(graphics)
        draw_clock(graphics, clock)
        draw_date(graphics, clock)
        pbar.draw(graphics)
        
        i75.update(graphics)
        time.sleep(0.025)
        

            
        
        if i75.switch_pressed(interstate75.SWITCH_B):
            from clock import NetworkTime
            from wifi import Wifi
            wc = Wifi()
            nt = NetworkTime(wc)
            nt.sync()

def get_display():
    return graphics
