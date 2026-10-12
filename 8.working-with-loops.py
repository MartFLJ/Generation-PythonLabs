# Exercise 1: Working with a while loop

import random


# Printing the game rules

print("Welcome to Guess the Number!")

print("The rules are simple. I will think of a number, and you will try to guess it.")


# Generating a random number

number = random.randint(1, 10)


# Tracking whether the guess is correct

isGuessRight = False


# Guessing loop

while isGuessRight != True:

    guess = input("Guess a number between 1 and 10: ")

    if int(guess) == number:

        print("You guessed {}. That is correct! You win!".format(guess))

        isGuessRight = True

    else:

        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))


# Exercise 2: Working with a for loop

print("Count to 10!")


# Counting from 0 to 10

for x in range(0, 11):

    print(x)
