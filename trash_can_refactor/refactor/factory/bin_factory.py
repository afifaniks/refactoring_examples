class BinFactory:
    def __init__(self):
        self._creators = {}

    def register_creator(self, key, creator):
        self._creators[key] = creator

    def create(self, key, **kwargs):
        creator = self._creators.get(key)
        if not creator:
            raise ValueError(key)
        return creator(**kwargs)
