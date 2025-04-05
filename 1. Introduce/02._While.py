#impor random
import random

print('-------------------------')
print('---- Guess the dice! ----')
print('-------------------------')

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

total = dice1 + dice2

#input tebakan
guess = int(input('What is the dice (2-12) : '))

#verifikasi tebakan
if guess < 2 or guess > 12:
    print('Invalid guess!')

#perulangan while
while guess != total:
    print('Try Again!')
    guess = int(input('What is the dice (2-12) : '))

if guess == total:
    print('You got it!')
