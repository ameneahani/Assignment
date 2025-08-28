
class Time():
    def __init__(self, second, minute, hour):
        self.second = second
        self.minute = minute
        self.hour = hour
        self.fix()

    def show(self):
        print(self.second, ":", self.minute, ":", self.hour)

    def sum(self, other):
        s_new = self.second + other.second
        m_new = self.minute + other.minute
        h_new = self.hour + other.hour
        time_new = Time(s_new, m_new, h_new)
        return time_new

    def sub(self, other):
        s_new = self.second - other.second
        m_new = self.minute - other.minute
        h_new = self.hour - other.hour
        time_new = Time(s_new, m_new, h_new)
        return time_new
    
    def time_to_second(self):
        second = self.hour *3600 + self.minute * 60 + self.second
        return second
        
    def GMT_to_Tehran(self):
        GMT = Time(3, 30, 0)
        return self.sum(GMT)

    def fix(self):
        if self.second >= 60:
            self.second -= 60
            self.minute += 1

        if self.minute >= 60:
            self.minute -= 60
            self.hour += 1

        if self.second <0:
            self.second += 60
            self.minute -= 1

        if self.minute <0:
            self.minute += 60
            self.hour -= 1




