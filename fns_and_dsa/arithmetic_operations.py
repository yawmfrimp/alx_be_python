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
