from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Cristina")
latte = Coffee("Latte")
mocha = Coffee("Mocha")

o1 = c1.create_order(latte, 4.5)
o3 = c1.create_order(mocha, 4.0)

print(o1)
print(o3)

print(c1.orders())    
print(c1.coffees())    

print(mocha.orders())  
print(mocha.customers()) 