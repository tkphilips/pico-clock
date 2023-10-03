
import interstate75
import time

from clock import Clock

DISPLAY_TYPE = interstate75.DISPLAY_INTERSTATE75_64X32

i75 = interstate75.Interstate75(display=DISPLAY_TYPE)
graphics = i75.display

#WHITE = graphics.create_pen(255, 255, 255)
WHITE = graphics.create_pen_hsv(1.0, 0.0, 0.5)
BLACK = graphics.create_pen(0, 0, 0)


def draw_clock(graphics, clock):
    print('draw', clock.time)
    graphics.set_font('bitmap8')
    graphics.set_pen(WHITE)
    graphics.text(clock.time, 0, 1, scale=2)

def draw_date(graphics, clock):
    print('draw', clock.date)
    graphics.set_font('bitmap4')
    graphics.set_pen(WHITE)
    graphics.text(clock.date, 10, 24, scale=1)

def clear_screen(graphics):
    graphics.set_pen(BLACK)
    graphics.clear()
    

def run_clock():
    while True:
        clock = Clock()
        
        clear_screen(graphics)
        draw_clock(graphics, clock)
        draw_date(graphics, clock)
        
        i75.update(graphics)
        time.sleep(1)

def get_display():
    return graphics
