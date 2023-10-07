
from colour import Green, Black

class ScrollMessage:
    def __init__(self, xy=(0, 0), max_lines=3):
        self.max_lines = max_lines
        self.xy = xy
        
        self._lines = []
    
    def render(self, display):
        lines = self._lines[:-1*self.max_lines]
        text = '\n'.join(lines)
        
        black = Black(display)
        black.use()
        display.clear()
        
        green = Green(display)
        green.use()
        
        display.set_font('bitmap4')
        
        display.text(text, *self.xy, scale=1)
        
    def print(self, i75, display, text):
        self._lines.append(text)
        #self.render(display)
        self.render(i75.display)
        i75.update(i75.display)
        
        
        
        
        