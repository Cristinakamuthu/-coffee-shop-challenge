class Coffee:
    def __init__(self, name):
        self._name = None
        self.name = name  

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if self._name is not None:
            raise ValueError("name is immutable")
        
        if not isinstance(name, str):
            raise ValueError("name must be a string")
        
        if not (1 <= len(name) <= 3):
            raise ValueError("name must be between 1-3 characters long")

        self._name = name

c1= Coffee("rte")
c1.name = "tis"
print(c1.name)