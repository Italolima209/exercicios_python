import random

print('=' * 12, 'Jokenpo Game', '=' * 12)

user_choice = input('\nChoose rock, paper or scissors: ').lower().strip()

if user_choice not in ['rock', 'paper', 'scissors']:
    print('Invalid option!')

else:
    cpu_choice = random.choice(['rock', 'paper', 'scissors'])

    print()

    if (
        user_choice == 'scissors' and cpu_choice == 'paper'
        or user_choice == 'rock' and cpu_choice == 'scissors'
        or user_choice == 'paper' and cpu_choice == 'rock'
    ):
        print('=' * 12, 'Player Won!', '=' * 12)

    elif user_choice == cpu_choice:
        print('=' * 12, 'Draw Game!', '=' * 12)

    else:
        print('=' * 12, 'CPU Won!', '=' * 12)

    print(f'The computer chose {cpu_choice}')