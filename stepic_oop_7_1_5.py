class Validator():
    def __init__(self, obj):
        self.obj = obj
    def is_valid(self):
        pass
class NumberValidator(Validator):
    def is_valid(self):
        return isinstance(self.obj,int|float)
