from art import logo

import random

randno = random.randint(1, 100)

guess = 0

def hint(guess):
    if guess > randno:
        print("Too high.")
    elif guess < randno:
        print("Too low.")
    elif guess == randno:
        print("Wow, that's correct!")
    return

ten = [10,9,8,7,6,5,4,3,2,1]
five = [5,4,3,2,1]

def easy():
    for i in ten:
        print(f"You have {i} attempts remaining to guess the number")
        print()
        guess = int(input("Make a guess: "))
        print()
        hint(guess)
        print()
        if guess == randno:
          break
def hard():
    for i in five:
        print()  
        print(f"You have {i} attempts remaining to guess the number")
        print()
        guess = int(input("Make a guess: "))
        print()
        hint(guess)
        if guess == randno:
          break

print(logo)
enter = input("Welcome to the guessing game where you're gonna guess the number I think,click ENTER to start.!")
print()
level = input("Choose a difficulty - Type easy or hard: ").lower()
print()
print("I'm thinking of a number between 1 and 100.")

if level == "easy":
    easy()
else:
    hard()

