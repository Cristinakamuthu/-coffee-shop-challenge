

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
       from order import Order
       return [order for order in Order.all_order if Order.customer ==  self]
    
    def coffees(self):
        from order import Order
        return list({order.coffee for order in  Order.all_orders if Order.customer == self})

    
def create_order(self, coffee, price):
    from order import Order
    return Order(self, coffee, price)


        
        

