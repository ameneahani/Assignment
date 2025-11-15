from datetime import datetime
import time
from zoneinfo import ZoneInfo
from PySide6.QtCore import QThread, Signal

class WorldClockThread(QThread):
    signal_worldclock = Signal(datetime)
    def __init__(self, city_worldclock):
        super().__init__()
        self.city_worldclock = city_worldclock

    def set_city(self, city_worldclock):
        self.city_worldclock = city_worldclock

    def run(self):
        while True:
            date_now = datetime.now(ZoneInfo(self.city_worldclock))
            time_now = date_now.strftime("%I: %M: %S %p")
            self.signal_worldclock.emit(time_now)
            time.sleep(1)

