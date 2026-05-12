n = int(input('\n\033[34mType a number to see the multiplication table: \033[m'))
print()

for j in range(1, 11):
    print(f'\033[33m{n}\033[m x \033[36m{j}\033[m = \033[32m{n * j}\033[m')

