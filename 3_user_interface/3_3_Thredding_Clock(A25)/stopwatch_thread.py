import time
from PySide6.QtCore import QThread, Signal
from mytime import Mytime

class StopWatchThread(QThread):
    signal_stopwatch = Signal(Mytime)
    def __init__(self):
        super().__init__()
        self.time = Mytime(0, 0, 0)
        

    def run(self):
        while True:
            time.sleep(1)
            self.time.plus()
            self.signal_stopwatch.emit(self.time)

    def reset(self):
        self.time = Mytime(0, 0, 0)
        self.signal_stopwatch.emit(self.time)

    
            
            
        

