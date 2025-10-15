def convert_temperature(value, unit):
    unit = unit.lower()

    if unit == 'c':  # Celsius
        fahrenheit = (value * 9/5) + 32
        kelvin = value + 273.15
        print(f"\n{value}°C = {fahrenheit:.2f}°F")
        print(f"{value}°C = {kelvin:.2f}K")

    elif unit == 'f':  # Fahrenheit
        celsius = (value - 32) * 5/9
        kelvin = celsius + 273.15
        print(f"\n{value}°F = {celsius:.2f}°C")
        print(f"{value}°F = {kelvin:.2f}K")

    elif unit == 'k':  # Kelvin
        celsius = value - 273.15
        fahrenheit = (celsius * 9/5) + 32
        print(f"\n{value}K = {celsius:.2f}°C")
        print(f"{value}K = {fahrenheit:.2f}°F")

    else:
        print("❌ Invalid unit! Please enter C, F, or K.")


print("🌡️ Temperature Conversion Program")
try:
    value = float(input("Enter the temperature value: "))
    unit = input("Enter the unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").strip()
    convert_temperature(value, unit)
except ValueError:
    print("❌ Please enter a valid number for temperature.")
