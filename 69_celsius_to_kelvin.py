# Convert Celsius to Kelvin
def celsius_to_kelvin(celsius):
    return celsius + 273.15

temp_celsius = 25
temp_kelvin = celsius_to_kelvin(temp_celsius)

print(f"{temp_celsius} degrees Celsius is equal to {temp_kelvin} Kelvin")
