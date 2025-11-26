# temp_conversion_tool.py
# You're now a temperature wizard!

# GLOBAL VARIABLES (they live at the top, everyone can see them!)
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FREEZING_POINT_OFFSET = 32  # This is how much we add/subtract

# Function 1: Fahrenheit → Celsius
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - FREEZING_POINT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Function 2: Celsius → Fahrenheit
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_OFFSET
    return fahrenheit

# MAIN PROGRAM — where the magic happens!
print("Temperature Converter 3000 Activated!")

try:
    # Ask for temperature
    temp_input = input("Enter the temperature to convert: ").strip()
    temperature = float(temp_input)  # Convert string to number

    # Ask for unit
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    # Do the conversion!
    if unit == "F":
        converted = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted:.2f}°C")
    
    elif unit == "C":
        converted = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted:.1f}°F")
    
    else:
        print("Please enter C or F only!")

except ValueError:
    print("Invalid temperature. Please enter a numeric value.")

print("Thanks for using Temperature Converter 3000!")