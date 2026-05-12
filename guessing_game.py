import random

print('\033[34m=-' * 7, 'Guessing Game', '-=' * 7, '\033[m')

user_number = int(input('\n\033[36mEnter a number between 0 and 5: \033[m'))

if user_number < 0 or user_number > 5:
    print('\033[31mInvalid option!\033[m')
else:

    cpu_number = random.randint(0, 5)

    print()

    if user_number > cpu_number:
        print('\033[31mYou lose!\033[m')
    elif user_number < cpu_number:
        print('\033[31mYou lose!\033[m')
    else:
        print('\033[32mYou win!\033[m')

    print(f'The number chosen by the computer was \033[33m{cpu_number}\033[m')

print('\n\033[34m' + '=-' * 8, 'Game Over', '-=' * 8, '\033[m')