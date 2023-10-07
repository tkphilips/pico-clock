import time
import ntptime

class Clock:
    def __init__(self):
        self.dt = Time()
    
    @property
    def time(self):
        t_str = '{0:02d}:{1:02d}:{2:02d}'.format(
            self.dt.hour,
            self.dt.minute,
            self.dt.second)
        
        return t_str
        
    
    @property
    def date(self):
        d_str = '{0}-{1:02d}-{2:02d}'.format(
            self.dt.year,
            self.dt.month,
            self.dt.day)
        
        return d_str

        
class Time:
    def __init__(self, timezone=1):
        t = time.localtime()
        t = time.localtime(time.time() + (3600 * timezone))
        
        self.year = t[0]
        self.month = t[1]
        self.day = t[2]
        self.hour = t[3]
        self.minute = t[4]
        self.second = t[5]
        
        
class NetworkTime:
    def __init__(self, wifi):
        self.wifi = wifi
    
    def connect(self):
        if self.wifi.isconnected():
            return
        
        self.wifi.connect()
        
        while not self.wifi.isconnected():
            print('ntp waiting for wifi...')
            time.sleep(3)
        
    def sync(self):
        self.connect()
        print(f'time before sync: {time.localtime()}')
        ntptime.settime()
        print(f' time after sync: {time.localtime()}')
        
        

