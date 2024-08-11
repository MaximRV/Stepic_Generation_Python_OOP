class Todo:
    def __init__(self):
        self.things = []

    def add(self, case: str, priority: int):
        self.things.append((case, priority))

    def get_by_priority(self, n):
        if self.things:
            return [i[0] for i in self.things if i[1] == n]
        else:
            return self.things

    def get_low_priority(self):
        if self.things:
            min_prior = min([i[1] for i in self.things])
            return [i[0] for i in self.things if i[1] == min_prior ]
        else:
            return self.things

    def get_high_priority(self):
        if self.things:
            max_prior = max([i[1] for i in self.things])
            return [i[0] for i in self.things if i[1] == max_prior]
        else:
            return self.things

todo = Todo()

todo.add('Ответить на вопросы', 5)
todo.add('Сделать картинки', 1)
todo.add('Доделать задачи', 4)
todo.add('Дописать конспект', 5)

print(todo.get_low_priority())
print(todo.get_high_priority())
print(todo.get_by_priority(3))