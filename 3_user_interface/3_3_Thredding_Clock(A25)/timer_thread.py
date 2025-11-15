import time
from PySide6.QtCore import QThread, Signal
from mytime import Mytime

class TimerThread(QThread):
    signal_timer = Signal(Mytime)
    signal_finished = Signal()

    def __init__(self, hour, minute, second):
        super().__init__()
        self.hour = hour
        self.minute = minute
        self.second = second
        self.time = Mytime(self.hour, self.minute, self.second)
        
        self.initial_hour = hour
        self.initial_minute = minute
        self.initial_second = second

        self.running = False

    def run(self):
        self.running = True
        while self.running:
            time.sleep(1)
            self.time.minus()
            self.signal_timer.emit(self.time)
            
            if self.time.hour == 0 and self.time.minute == 0 and self.time.second == 0:
                self.signal_finished.emit()
                self.running = False
                break    

    def reset(self):
        self.time.hour = self.initial_hour
        self.time.minute = self.initial_minute
        self.time.second = self.initial_second
        self.signal_timer.emit(self.time)

    def set_time(self, hour, minute, second):
        self.time.hour = hour
        self.time.minute = minute
        self.time.second = second

        self.initial_hour = hour
        self.initial_minute = minute
        self.initial_second = second

    
        
        
        
        



