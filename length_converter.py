green = "\033[32m"
red = "\033[31m"
yellow = "\033[33m"
blue = "\033[34m"
cyan = "\033[36m"
reset = "\033[m"

print(f'\n{blue}' + '=' * 10 + ' Length Converter ' + '=' * 10 + f'{reset}\n')

meters = float(input(f'{cyan}Enter a measurement in meters: {reset}'))

km = meters / 1000
hm = meters / 100
cm = meters * 100
mm = meters * 1000

print(f'''
{green}{meters} meters is equal to:{reset}
- {yellow}{km} km{reset}
- {yellow}{hm} hm{reset}
- {yellow}{cm} cm{reset}
- {yellow}{mm} mm{reset}
''')