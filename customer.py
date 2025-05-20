from order import order

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
    
    def orders(self):
       return [order for order in order.all_order if order.customer ==  self]
    
    def coffees(self):
        return list({order.coffee for order in  order.all_orders if order.customer == self})

    def create_order(self, coffee, price):
        return(self,coffee, price)
    
        
        
        

c1 = Customer("Tiekkjikiojuokjtkoiyokkihjkujotokutlmkojmukmik6m")
print(c1.name)