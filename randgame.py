import random
import sys
wordList = ["elephant","blanket", "chair", "pillow", "sheet",
"paper", "airpods", "watch","laptop", "gun", "hamlet", "hammer", "wire",
"rifle", "hat"]
guess_word = []
secretWord = random.choice(wordList)
from thelist
length_word = len(secretWord)
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_storage = []
def beginning():
 print("Hello Mate!\n")
 while True:
 name = input("Please enter Your name\n").strip()
 if name == '':
 print("No blank lines")
 else:
 break
beginning()
def newFunc():
 print("Well, that's perfect moment to play some Hangman!\n")
 while True:
 gameChoice = input("Would You?\n").upper()
 if gameChoice == "YES" or gameChoice == "Y":
 break
 elif gameChoice == "NO" or gameChoice == "N":
 sys.exit("Have a nice day")
 else:
 print("Please Answer only Yes or No")
 scontinue
newFunc()
def change():
 for character in secretWord:
 guess_word.append("-")
print("Ok, so the word You need to guess has", length_word,"characters")
print("Be aware that You can enter only 1 letter from a-z\n\n")
print(guess_word)
def guessing():
 guess_taken = 1
 while guess_taken < 10:
 guess = input("Pick a letter\n").lower()
 if not guess in alphabet:
 print("Enter a letter from a-z alphabet")
 elif guess in letter_storage: 
  print("You have already guessed that letter!")
else:
letter_storage.append(guess)
if guess in secretWord:
 print("You guessed correctly!")
 for x in range(0, length_word):
   if secretWord[x] == guess:
     guess_word[x] = guess
     print(guess_word)
  if not '-' in guess_word:
    print("You won!")
 break

 else:
 print("The letter is not in the word. Try Again!")
 guess_taken += 1
 if guess_taken == 10:
 print(" The word was",secretWord)
change()
guessing()
print("Game Over!")
