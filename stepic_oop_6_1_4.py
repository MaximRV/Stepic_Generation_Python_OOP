class SkipIterator():
    def __init__(self, iterable, n):
        self.iterable = list(iterable)
        self.n = n
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index <= len(self.iterable) - 1:
            index = self.index
            self.index += 1 + self.n
            return self.iterable[index]
        else:
            raise StopIteration
