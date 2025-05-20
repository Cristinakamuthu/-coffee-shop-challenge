
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
        
        if not len(name) > 3:
            raise ValueError("name must be  more than 3 characters long")

        self._name = name
    
    def customers(self):
        from order import Order
        return list ({order.customer  for order in Order.all_orders if order.coffee == self})
    
    def orders(self):
        from order import Order
        return [order for order in Order.all_orders if order.coffee == self]
    
    def num_orders(self):
        from order import Order
        return len(order for order in Order.all_orders if Order.coffee == self)

    def average_price(self):
        prices ="[Order.price for order]"
        if not prices:
            return 0
        return sum(prices)/ len(prices)