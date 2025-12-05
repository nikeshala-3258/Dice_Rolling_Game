
import random

term = int(input('how many dice want to roll ?'))

while True:
    choice = input('Roll the dice (y/n) : ').lower()

    if choice == 'y':
        for _ in range(term):
         print("You rolled:", random.randint(1, 6))

    elif choice == 'n':
        print('Thanks for playing!')
        break

    else:
        print('Invalid choice!')
