#import the random lib
import random

#define a function
def computer_guess(x):
  feedback = " "
  
  #assign variable of range 
  low = 1
  high = x

  while feedback != "c":
    #let computer have a random guess and check not equal low and high
    if low != high:  
      guess = random.randint(low, high)
    else:
      guess = low
    print(f"The guess is: {guess}")

    #check if the guess is too low, too high or correct
    feedback = input("Enter Correct(C), too low(L) or too high(H): ").lower()
    if feedback == "h":
      high = guess - 1
    elif feedback == "l":
      low = guess + 1
  
  print(f"The computer guessed your number {guess}.")

print("Pick a number between 1 and 100. In this game, computer is going to guess the number. Please provide feedback using letters to play the game")

start = input("Are you ready ? Press yes(Y) or no(N):  ").lower()

if start == "y":
  computer_guess(100)
elif start == "n":
  print("You entered no and the game is quiting.")