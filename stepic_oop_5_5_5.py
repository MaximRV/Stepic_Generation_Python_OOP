class Queue:
    def __init__(self, *args):
        self.queue = list(args)

    def add(self, *args):
        self.queue.extend(args)

    def pop(self):
        if self.queue:
            return self.queue.pop(0)
        return None

    def __str__(self):
        return ' -> '.join([str(i) for i in self.queue])

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.queue == other.queue
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(*self.queue +other.queue)
        return  NotImplemented


    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            self.queue.extend(other.queue)
            return self
        return NotImplemented

    def __rshift__(self, other):
        if isinstance(other,int):
            if other >= len(self.queue):
                return self.__class__()
            return self.__class__(*self.queue[other:])
        return NotImplemented
