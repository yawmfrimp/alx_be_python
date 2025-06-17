FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    temperature = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)
    return temperature

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    temperature = (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) + 32
    return temperature

if __name__ == '__main__':
    try:
        a = float(input("Enter the temperature to convert: "))
    except ValueError:
        print('Invalid temperature')
        exit()
    temperature_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
    match temperature_unit:
        case 'C':
            print(f'{a}C is {convert_to_fahrenheit(a):.2f}F')
        case 'F':
            print(f'{a}F is {convert_to_celsius(a):.2f}C')
        case _:
            print("Input is invalid. Enter a valid temperature unit")

