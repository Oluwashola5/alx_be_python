# # Define global conversion factors
# FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
# CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# def convert_to_celsius(fahrenheit):
#     """
#     Converts a temperature from Fahrenheit to Celsius.
#     """
#     return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# def convert_to_fahrenheit(celsius):
#     """
#     Converts a temperature from Celsius to Fahrenheit.
#     """
#     return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# def main():
#     try:
#         # Get user input
#         temperature = input("Enter the temperature to convert: ").strip()
#         if not temperature.replace('.', '', 1).isdigit():
#             raise ValueError("Invalid temperature. Please enter a numeric value.")
#         temperature = float(temperature)

#         unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

#         # Determine the conversion
#         if unit == "C":
#             converted_temp = convert_to_fahrenheit(temperature)
#             print(f"{temperature}°C is {converted_temp}°F")
#         elif unit == "F":
#             converted_temp = convert_to_celsius(temperature)
#             print(f"{temperature}°F is {converted_temp}°C")
#         else:
#             raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
#     except ValueError as e:
#         print(e)

# if __name__ == "__main__":
#     main()

# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Get user input
        temperature = input("Enter the temperature to convert: ").strip()
        if not temperature.replace('.', '', 1).isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        temperature = float(temperature)

        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Determine the conversion
        if unit == "C":
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        elif unit == "F":
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

