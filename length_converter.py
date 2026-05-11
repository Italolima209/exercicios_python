print('\n', '=' * 10, 'Length Converter', '=' * 10)

meters = float(input('Enter a measurement in meters: '))

km = meters / 1000
hm = meters / 100
cm = meters * 100
mm = meters * 1000

print(f'''
{meters} meters is equal to:
- {km} km
- {hm} hm
- {cm} cm
- {mm} mm
''')