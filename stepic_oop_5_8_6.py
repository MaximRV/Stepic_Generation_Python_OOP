
class AttrsNumberObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
    def __getattr__(self, item):
        if item == "attrs_num":
            return len(self.__dict__) + 1
        return AttributeError
