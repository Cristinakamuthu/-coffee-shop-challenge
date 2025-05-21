class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def orders(self):
        from order import Order
        return [order for order in Order.all_orders if order.customer == self]

    def coffees(self):
        from order import Order
        return list({order.coffee for order in Order.all_orders if order.customer == self})

    def create_order(self, coffee, price):
        from order import Order
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        from order import Order 

        spending = {}

        for order in Order.all_orders:
            if order.coffee == coffee:
                spending[order.customer] = spending.get(order.customer, 0) + order.price

        if not spending:
            return None
        
        return max(spending, key=spending.get)


