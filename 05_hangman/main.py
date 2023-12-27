import random
from words import words
import string

def get_valid_word(words):
  word = random.choice(words)
 
  while '-' in word:
    word = random.choice(words)
 
  return word.upper()

def hangman():

  alphabets = set(string.ascii_uppercase)
  
  word = get_valid_word(words)
  letter_in_word = set(word)

  used_letter = set()

  print(word)

  lives = 10

  while len(letter_in_word) > 0 and lives > 0:

    print("You have", lives , "lives left. You used the following letters: ", ' '.join(used_letter))

    current_word = [letter if letter in used_letter else '-' for letter in word]
    print("The word is:", ' '.join(current_word))

    guess = input("Guess a letter: ").upper()

    if guess in alphabets - used_letter:
      used_letter.add(guess)
      #print("guessed word is not present in used words")

      if guess in letter_in_word:
        letter_in_word.remove(guess)
        print("Your guessed word is present in the word.")
      else:
        lives = lives - 1
        print("Your guessed letter is not present in the word.")

    elif guess in used_letter:
      print("You already used this letter.")

    else:
      print("Invalid character.")
  
  #reach here if length of letters_in_word is zero
  if lives > 0:
    print("You gussed the word: ", word)
  else:
    print("You run out of lives and died. The word was: ", word)


#call the game function
hangman()