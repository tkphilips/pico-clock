import time

class Clock:
    def __init__(self):
        self.dt = Time()
    
    @property
    def time(self):
        t_str = '{0}:{1}:{2}'.format(
            self.dt.hour,
            self.dt.minute,
            self.dt.second)
        
        return t_str
        
    
    @property
    def date(self):
        d_str = '{0}-{1}-{2}'.format(
            self.dt.year,
            self.dt.month,
            self.dt.day)
        
        return d_str

        
class Time:
    def __init__(self):
        t = time.localtime()
        
        self.year = t[0]
        self.month = t[1]
        self.day = t[2]
        self.hour = t[3]
        self.minute = t[4]
        self.second = t[5]
        

