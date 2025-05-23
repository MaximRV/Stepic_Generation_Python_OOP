from functools import total_ordering


@total_ordering
class Word:
    def __init__(self, word):
        self.word = word

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.word}')"

    def __str__(self):
        return self.word[0].upper() + self.word[1:].lower()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return len(self.word) == len(other.word)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return len(self.word) < len(other.word)
        return NotImplemented


