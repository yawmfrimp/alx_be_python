<<<<<<< HEAD
def perform_operation(num1,num2,operation):
  
    match operation:
        case "add":
            return (num1 + num2)
        case "subtract":
            return (num1 - num2)
        case "multiply":
            return (num1 * num2)
        case "divide":
            while num2 != 0:
                return (num1 / num2)

print(perform_operation(0, 1,'divide'))
=======
def perform_operation(num1, num2, operation):
  
     if operation == 'add':
        return (num1 + num2)
    elif operation == 'subtract':
        return (num1 - num2)
    elif operation == 'multiply':
        return (num1 * num2)
    elif operation == 'divide':
        while num2 == 0:
            print(f'Error: cannot divide by zero')
            break
        else:
            return (num1 / num2)
>>>>>>> faeea08ddb5bd909c36e4f1a5bd5fb98d41e33e8
