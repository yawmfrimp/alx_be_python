def add(x,y):
    return x+y

def subtract(x,y):
    return(x-y)

def multiply(x,y):
    return(x*y)

def divide(x,y): #modifyied the code to raise an exception when y == 0
    if y == 0:
        raise ZeroDivisionError("Cannot divide by Zero")

    return(x/y)

