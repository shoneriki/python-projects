# tutorial of  kying18
import random
from words import words
import string

def get_valid_word(words):
  word = random.choice(words)
  while '-' in word or ' ' in word:
    word = random.choice(words)

  return word.upper()

def hangman():
  word = get_valid_word(words)
  word_letters = set(word)
  alphabet = set(string.ascii_uppercase)
  used_letters = set()
  
  while len(word_letters) > 0:
    # letters used
    # ' '.join(['a', 'b', 'c']) --> 'a b c'
    print('You have used these letters ', ' '.join(used_letters))

    # what current word is (ie W - A T)
    word_list = [letter if letter in used_letters else '-' for letter in word]
    print('Current word: ', ' '.join(word_list))

    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabet - used_letters:
      used_letters.add(user_letter)
      if user_letter in word_letters:
        word_letters.remove(user_letter)

    elif user_letter in used_letters:
      print('You have already used that character. Try again.')

    else:
      print('Invalid character. Try again.')

hangman()
