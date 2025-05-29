from datetime import date

class DateFormatter:
    __data = {
        "ru": "%d.%m.%Y",
        "us": "%m-%d-%Y",
        "ca": "%Y-%m-%d",
        "br": "%d/%m/%Y",
        "fr": "%d.%m.%Y",
        "pt": "%d-%m-%Y"}

    def __init__(self, country_code):
        self.country_code = country_code

    def __call__(self, d: date):
        return d.strftime(self.__data[self.country_code])

