
class ProgressBar:
    def __init__(self, x, y, width, min_val, max_val):
        self.x = x
        self.y = y
        self.max_width = width
        
        self.min_val = min_val
        self.max_val = max_val
        
        self.range = 1.0 * (max_val - min_val)
        
        self.value = 0
    
    def set_progress(self, value):
        self.value = value
    
    
    def draw(self, graphics):
        print('draw line', *self.line_coords)
        graphics.line(*self.line_coords)
    
    @property
    def width(self):
        current = (1.0 * self.value) - self.min_val
        pct = current / self.range
        
        return int(self.max_width * pct)
    
    @property
    def line_coords(self):
        x2 = self.x + self.width
        return (self.x, self.y, x2, self.y)
        
        