green = "\033[32m"
red = "\033[31m"
yellow = "\033[33m"
blue = "\033[34m"
cyan = "\033[36m"
reset = "\033[m"

print(f'\n{blue}' + '=' * 10 + ' Temperature Converter ' + '=' * 10 + f'{reset}')

celsius = float(input(f'\n{cyan}Enter temperature in °C: {reset}'))

fahrenheit = celsius * 1.8 + 32
kelvin = celsius + 273.15

print(f'''
{green}Temperature conversion:{reset}
- {yellow}{celsius:.2f} °C{reset}
- {yellow}{fahrenheit:.2f} °F{reset}
- {yellow}{kelvin:.2f} K{reset}
''')