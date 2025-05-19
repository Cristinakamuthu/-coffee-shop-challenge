class Order:
    def __init__(self, customer, coffee, price):
        self._customer = customer
        self._coffee = coffee
        self.price = price  

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if isinstance(price, float):
            if 1.0 <= price <= 10.0:
                self._price = price
            else:
                raise ValueError("the price must be between 1.0 - 10.0")
        else:
            raise ValueError("the price must be a float")
        
c1 = Order("Tom","Mocha","15.4")
print(c1)
