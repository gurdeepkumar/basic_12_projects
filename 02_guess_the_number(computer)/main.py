#import the lib for random number 
import random

#let the computer generate a radom number in a range
def guess(x):
  random_number = random.randint(1, x)
  guess_number = 0
  while guess_number != random_number:
    #ask the user to input a number to guess
    guess_number = int(input("Enter a guess: "))
    #check if the number is too low or high
    if guess_number < random_number:
      print("The number is too low.")
    elif guess_number > random_number:
      print("The number is too high.")
  #check if the number is right
  print("Congrats, you guessed the number.")

#call the guess function
guess(10)

