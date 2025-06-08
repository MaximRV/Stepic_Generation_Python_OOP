class NonNegativeObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __setattr__(self, key, value):
        if isinstance(value, int|float):
            object.__setattr__(self, key, abs(value))
        else:
            object.__setattr__(self, key, value)