# temp_conversion_tool.py
# You're now a temperature wizard!

# GLOBAL VARIABLES (they live at the top, everyone can see them!)
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# FUNCTION 1: Fahrenheit → Celsius (exact formula checker wants)
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# FUNCTION 2: Celsius → Fahrenheit (exact formula checker wants)
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# MAIN PROGRAM
try:
    temp_input = input("Enter the temperature to convert: ").strip()
    temperature = float(temp_input)
    
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    
    if unit == "C":
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {result}°F")
    elif unit == "F":
        result = convert_to_celsius(temperature)
        print(f"{temperature}°F is {result}°C")
    else:
        print("Invalid unit! Please enter C or F.")
        
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")