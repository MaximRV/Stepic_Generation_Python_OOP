class AnyClass:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f'AnyClass: {", ".join([f"{k}={repr(v)}" for k, v in self.__dict__.items()])}'

    def __repr__(self):
        return f'AnyClass({", ".join([f"{k}={repr(v)}" for k, v in self.__dict__.items()])})'

obj = AnyClass(attr1=10, attr2='beegeek', attr3=True, attr4=[1, 2, 3], attr5=('one', 'two'), attr6=None)

print(str(obj))
print(repr(obj))