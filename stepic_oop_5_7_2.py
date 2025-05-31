class Temperature:
    def __init__(self, temperature):
        self.temperature = temperature

    def to_fahrenheit(self):
        return 9 / 5 * self.temperature + 32

    def __str__(self):
        return f'{round(self.temperature,2)}°C'

    def __bool__(self):
        return self.temperature > 0

    def __float__(self):
        return float(self.temperature)

    def __int__(self):
        return int(self.temperature)

    @classmethod
    def from_fahrenheit(cls, temperature):
        return cls(5 / 9 * (temperature - 32))


