class Processor:
    @staticmethod
    def process(data):
        if isinstance(data, (int, float)):
            return data * 2
        elif isinstance(data, str):
            return data.upper()
        elif isinstance(data, list):
            return sorted(data)
        elif isinstance(data, tuple):
            return tuple(sorted(data))
        raise TypeError('Аргумент переданного типа не поддерживается')