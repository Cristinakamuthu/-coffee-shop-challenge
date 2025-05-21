from customer import Customer
from coffee import Coffee

class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        self._set_customer(customer)
        self._set_coffee(coffee)
        self._set_price(price)
        Order.all_orders.append(self)

    def _set_customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise ValueError("Customer must be a valid Customer instance.")

    def _set_coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            raise ValueError("Coffee must be a valid Coffee instance.")

    def _set_price(self, price):
        if isinstance(price, float) and 1.0 <= price <= 10.0:
            self._price = price
        else:
            raise ValueError("Price must be a float between 1.0 and 10.0.")

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price
