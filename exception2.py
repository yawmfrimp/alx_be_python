#so in this one we create a class which inherits from the exceptions in order to create our own exception
class ValuetooHigh(Exception):
    def __init__(self):
        self
        
        

try:
    a = int(input("Input a number not greater than 100"))
    if a > 100:
        raise ValuetooHigh
except ValuetooHigh:
    print('Masa you no dey see what them rep?')
except ValueError:
    print('number pleasej')
