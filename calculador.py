green = "\033[32m"
red = "\033[31m"
yellow = "\033[33m"
blue = "\033[34m"
cyan = "\033[36m"
reset = "\033[m"

print(f'{blue}\n' + '=' * 10 + ' Calculador ' + '=' * 10 + f'{reset}\n')

n1 = int(input(f'{cyan}Enter a value: {reset}'))
n2 = int(input(f'{cyan}Enter another value: {reset}'))

add = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2

print(f'''{yellow}{n1} + {n2} = {add}{reset}
{yellow}{n1} - {n2} = {sub}{reset}
{yellow}{n1} x {n2} = {mult}{reset}
{yellow}{n1} / {n2} = {div:.1f}{reset}
''')