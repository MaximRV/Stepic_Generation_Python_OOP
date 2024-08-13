class Wordplay:
    def __init__(self, words=None):
        if words is None:
            words = []
        self.words = words[:]

    def add_word(self, word: str):
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, n: int):
        return  [i for i in self.words if len(i) == n]

    def only(self, *args):
        return [i for i in self.words if set(list(i)).issubset(set(list(args)))]

    def avoid(self, *args):
        return [i for i in self.words if  set(list(i)).isdisjoint(set(list(args)))]


wordplay = Wordplay(['a', 'arthur', 'timur', 'bee', 'geek', 'python', 'stepik'])

print(wordplay.words)
wordplay.add_word('stepik')
wordplay.add_word('bee')
wordplay.add_word('geek')
print(wordplay.words)