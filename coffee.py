class Coffee:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Name must be a string with at least 3 characters.")
        self._name = name  

    @property
    def name(self):
        return self._name

    def customers(self):
        from order import Order
        return list({order.customer for order in Order.all_orders if order.coffee == self})

    def orders(self):
        from order import Order
        return [order for order in Order.all_orders if order.coffee == self]

    def num_orders(self):
        from order import Order
        return len([order for order in Order.all_orders if order.coffee == self])

    def average_price(self):
        from order import Order
        prices = [order.price for order in Order.all_orders if order.coffee == self]
        if not prices:
            return 0
        return sum(prices) / len(prices)
