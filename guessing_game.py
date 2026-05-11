import random

print('=' * 7, 'Guessing Game', '=' * 7)

user_number = int(input('\nEnter a number between 0 and 5: '))

if user_number < 0 or user_number > 5:
    print('Invalid option!')
else:

    cpu_number = random.randint(0, 5)

    if user_number > cpu_number:
        print('You lose!')
    elif user_number < cpu_number:
        print('You lose!')
    else:
        print('You win!')

    print(f'The number chosen by the computer was {cpu_number}')

print('\n','=' * 8, 'Game Over', '=' * 8)    





