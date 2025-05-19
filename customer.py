class Customer:
    def __init__(self, name):
        self.name = name 
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            if 1 <= len(name) <= 15:
                self._name = name
            else:
                raise ValueError("name should be between 1 - 15 characters")
        else:
            raise ValueError("name should be a string")

c1 = Customer("Tiekkjikiojuokjtkoiyokkihjkujotokutlmkojmukmik6m")
print(c1.name)