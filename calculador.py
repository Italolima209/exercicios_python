print('\n', '=' * 10, 'Calculador', '=' * 10, '\n')

n1 = int(input('Enter a value: '))
n2 = int(input('Enter another value: '))

add = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2

print(f'{n1} + {n2} = {add}')
print(f'{n1} - {n2} = {sub}')
print(f'{n1} x {n2} = {mult}')
print(f'{n1} / {n2} = {div:.2f}')