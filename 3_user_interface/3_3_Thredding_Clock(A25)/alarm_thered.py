import time
from datetime import datetime
from PySide6.QtCore import QThread, Signal

class AlarmThread(QThread):
    signal_alarm = Signal(str, str)
    def __init__(self, alarms):
        super().__init__()
        self.running = False
        self.alarms = alarms

    def run(self):
        self.running = True
        while self.running:
            self.time_now = datetime.now()
            for alarm in self.alarms:
                parts = alarm[1].split(":")
                hour = parts[0]
                minute = (parts[1].split(" "))[0]
                
                if int(hour) == int(self.time_now.hour) and int(minute) == int(self.time_now.minute):
                    self.signal_alarm.emit(hour, minute)                    
                    time.sleep(60)
                   
            time.sleep(1)

    def stop(self):
        self.running = False