import random
import time

print("Welcome to the number guessing game")
time.sleep(2)
print('I am thinking of a number between 1 and 100')
time.sleep(2)
IsWin = False
shouldAsk = True
number = random.randint(1, 100)
while shouldAsk:
    level = input("select difficulty level: Type 'easy' or 'Hard' : ")
    if level.lower() == 'easy' or level.lower() == 'hard':
        shouldAsk = False
if level.lower() == 'easy':
    attempts = 10
    time.sleep(1)
    for i in range(10):
        print(f"you have {attempts} attempts")
        guess = int(input("Guess a number: "))
        if guess == number:
            print('CORRECT!! You guessed right')
            IsWin = True
            break
        elif guess < number and attempts > 1:
            print('Too low.')
            print('Guess again')
        elif attempts > 1:
            print('Too high')
            print('guess again')
        attempts -= 1
else:
    attempts = 5
    time.sleep(1)
    for i in range(5):
        print(f"you have {attempts} attempts")
        guess = int(input("Guess a number: "))
        if guess == number:
            print('CORRECT!! You guessed right')
            IsWin = True
            break
        elif guess < number and attempts > 1:
            print('Too low.')
            print('Guess again')
        elif attempts > 1:
            print('Too high')
            print('guess again')
        attempts -= 1
if not IsWin:
    print("You've run out of attempts!! Try again.")
