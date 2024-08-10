class TextHandler:
    def __init__(self):
        self.mylist = []
        self.min_list = []
        self.max_list = []

    def add_words(self, li):
        self.mylist.extend(li.split())

    def get_shortest_words(self):
        for i in self.mylist:
            if len(i) == len(min(self.mylist, key=len)):
                self.min_list.append(i)
        return self.min_list

    def get_longest_words(self):
        for i in self.mylist:
            if len(i) == len(max(self.mylist, key=len)):
                self.max_list.append(i)
        return self.max_list


texthandler = TextHandler()

texthandler.add_words('The world will hold my trial for your sins')
texthandler.add_words('Never meant to see the sky never meant to live')

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())
