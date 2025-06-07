class DefaultObject:
    def __init__(self, default=None, **kwargs):
        self.default = default
        self.attrList = kwargs
        self.__dict__.update(kwargs)

    def __getattr__(self, item):
        return self.default

