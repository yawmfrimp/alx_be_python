class product: #defining a class called product 
    def __init__(self,name,price,quantity):
        self.name = name #defining product name
        self.price = price #defining product price
        self.quantity = quantity #defining product quantity

    def product_value(self): #finding the value of the quantity of products in stock
        value = f'The total value of {self.name} is ${self.price * self.quantity:.2f}'
        return value 
    
product1 = product('chair',price=15.50, quantity=3) #1 instance using keyword arguments. makes for easy readability
product2 = product('table',25.70,13) #2 instance using positional arguments

print(product2.product_value())