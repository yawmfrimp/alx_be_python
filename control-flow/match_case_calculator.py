num1 = int(input("Enter the first number: ")) #prompt for first number
num2 = int(input("Enter the second number: ")) #prompt for second number 
operation = input("Choose the type of operation (+, -, *, /): ") #prompt for the operation involved

match operation:
    case "+":
        print(f'The result is {num1 + num2}')
    case "-":
        print(f'The result is {num1 - num2}')
    case "*":
        print(f'The result is {num1 * num2}')
    case "/":
        if num2 == 0:
            print("Cannot divide by zero")
        print(f'The result is {num1 / num2}')