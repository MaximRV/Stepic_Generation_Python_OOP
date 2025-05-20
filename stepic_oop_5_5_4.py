class Time:
    def __init__(self, hours, minutes):
        self.hours, self.minutes = Time._normalize(hours, minutes)

    @staticmethod
    def _normalize(hours, minutes):
        return (hours + minutes // 60) % 24, minutes % 60

    def __str__(self):
        return f'{self.hours:>02}:{self.minutes:>02}'

    def __add__(self, other):
        if isinstance(other, Time):
            hours, minutes = self._normalize(self.hours + other.hours, self.minutes + other.minutes)
            return Time(hours, minutes)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Time):
            self.hours, self.minutes = self._normalize(self.hours + other.hours, self.minutes + other.minutes)
            return self
        return NotImplemented

