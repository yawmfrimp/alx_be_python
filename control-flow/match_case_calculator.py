<<<<<<< HEAD
num1 = int(input("Enter the first number: ")) #prompt for first number
num2 = int(input("Enter the second number: ")) #prompt for second number 
operation = input("Choose the operation (+, -, *, /): ") #prompt for the operation involved

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
=======
num1 = int(input("Enter the first number: ")) #prompt for first number
num2 = int(input("Enter the second number: ")) #prompt for second number 
operation = input("Choose the operation (+, -, *, /): ") #prompt for the operation involved

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
>>>>>>> faeea08ddb5bd909c36e4f1a5bd5fb98d41e33e8
        print(f'The result is {num1 / num2}')