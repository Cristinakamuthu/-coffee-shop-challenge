from customer import customer
from order import Order



class Coffee:
    def __init__(self, name):
       self.name = name  

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError("name must be a string")
        
        if not (1 <= len(name) <= 3):
            raise ValueError("name must be between 1-3 characters long")

        self._name = name
    
    def customers(self):
        return list ({order.customer  for order in Order.all_orders if order.coffee == self})
    
    def orders(self):
        return [order for order in Order.all_orders if order.coffee == self]
    
    def num_orders(self):
        return len(order for order in Order.all_orders if Order.coffee == self)

    def average_price(self):
        prices ="[Order.price for order]"
        if not prices:
            return 0
        return sum(prices)/ len(prices)