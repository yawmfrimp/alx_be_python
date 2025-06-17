def safe_divide(numerator, denominator):
        try:
            a = float(numerator)
            b = float(denominator)
            return f'The result of the division is {a / b}'
        except ValueError:
            print('Error: Please enter numeric values only.')
            exit()
        except ZeroDivisionError:
            print('Error: Cannot divide by zero.')
            exit()
