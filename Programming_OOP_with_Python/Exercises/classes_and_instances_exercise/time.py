class Time:
    max_minutes = max_seconds = 59
    max_hours = 23

    def __init__(self, h, m, s):
        self.hours = h
        self.minutes = m
        self.seconds = s

    def set_time(self, h, m, s):
        self.hours = h
        self.minutes = m
        self.seconds = s

    def get_time(self):
        return f"{f'0{self.hours}' if self.hours <= 9 else self.hours}:{f'0{self.minutes}' if self.minutes <= 9 else self.minutes}" \
               f":{f'0{self.seconds}' if self.seconds <= 9 else self.seconds}"

    def next_second(self):
        self.seconds += 1
        if self.seconds == Time.max_seconds+1:
            self.seconds = 0
            self.minutes += 1
            if self.minutes == Time.max_minutes+1:
                self.minutes = 0
                self.hours += 1
                if self.hours == Time.max_hours+1:
                    self.hours = 0

        return self.get_time()



