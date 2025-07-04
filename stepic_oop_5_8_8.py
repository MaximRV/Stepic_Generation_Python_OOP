class ProtectedObject:
    def __init__(self,**kwargs):
        for k, v in kwargs.items():
            object.__setattr__(self, k, v)

    def __setattr__(self, key, value):
        if key.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        object.__setattr__(self, key, value)

    def __getattribute__(self, item:str):
        if item.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        return object.__getattribute__(self,item)

    def __delattr__(self, item):
        if item.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        object.__delattr__(self,item)
