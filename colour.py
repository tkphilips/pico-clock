
class Colours:
    def __init__(self, display):
        self.white = White(display)
        self.black = Black(display)
    
    def set_brightness(self, brightness):
        self.white.set_brightness(brightness)
        self.black.set_brightness(brightness)
        

class Colour:
    HUE = 0.0
    SAT = 0.0
    
    def __init__(self, display, brightness=1.0):
        self.display = display
        self.brightness = brightness
        
        self._pen = None
    
    @property
    def hsv(self):
        return (self.HUE, self.SAT, self.brightness)
    
    @property
    def pen(self):
        if self._pen is not None:
            return self._pen
        
        self._pen = self.display.create_pen_hsv(*self.hsv)
        return self._pen
    
    def set_brightness(self, brightness):
        self._pen = None
        self.brightness = brightness
    
    def use(self):
        self.display.set_pen(self.pen)
        
    

class White(Colour):
    HUE = 1.0
    SAT = 0.0

class Green(Colour):
    HUE = 0.33333
    SAT = 1.0


class Black(Colour):
    HUE = 0.0
    SAT = 0.0
    