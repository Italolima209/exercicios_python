print('\n', '=' * 10, 'Temperature converter', '=' * 10)

celsius = float(input('\nEnter the temperature in °C: '))

fahrenheit = celsius * 1.8 + 32
kelvin = celsius + 273.15

print(f'''
Temperature conversion:
- {celsius:.2f} °C
- {fahrenheit:.2f} °F
- {kelvin:.2f} K
''')