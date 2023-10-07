
import network
import time

import secrets

class Wifi(network.WLAN):
    def __init__(self):
        self.creds = secrets.SSID
        
        super().__init__(network.STA_IF)
    
    def connect(self):
        if not self.active():
            self.active(True)
            
        super().connect(self.creds.SSID,
                        self.creds.PASSWORD)
