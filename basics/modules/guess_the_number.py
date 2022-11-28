print("Please enter the minimum value: ")
min_number = int(input())

print("Please enter the maximum value: ")
max_number = int(input())

import random

random_number = random.randrange(min_number, max_number)
print("I am thinking of a number between {} and {}.".format(min_number, max_number))
print("Can you guess what it is?")

guess = 0
while (guess != random_number):
  print("Please enter the number: ")
  guess = int(input())
  if (guess == random_number):
    print("Congratulations!You guessed my number!")
    break
  elif (guess > random_number):
    print("Your guess is too high.")
  elif (guess < random_number):
    print("Your guess is to low.")
  else: 
    print("Try again!")

print("Game Over!")
