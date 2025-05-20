from customer import Customer
class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price  
        Order.all_orders.append(self)

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
    
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        if not isinstance (customer, customer):
            return ValueError("Customer must be an instance of customer")
        
    @property
    def coffee(self, coffee):
        return self._coffee
    
    @coffee.setter
    def coffee(self,coffee):
        if not isinstance(coffee, coffee):
            return ValueError("coffee must be an instance of coffee")
    @property
    def price(self, price):
        return self._price
    
    @price.setter
    def price (self, price):
        if not isinstance(price, price):
            return ValueError("price must be an instance of price ")
    

        
c1 = Order("Tom","Mocha","15.4")
print(c1)
