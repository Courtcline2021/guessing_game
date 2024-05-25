#Modules to be imported into game 
import time
import random 
from collections import Counter 

# user adds name to display at the top of game 
user = input("Enter your name:")
print("Welcome to the game " + user)

time.sleep(1)

print("Time to start guessing!")
time.sleep(0.5)
#words that will be randomly selected was liking of a list but dictionary works better because I can add clues for the words 
some_words = """python api cpu html javascript pythondeveloper laptop 
remote lists function oop backend files  """
some_words = some_words.split(' ')
word = random.choice(some_words)

if __name__ == '__main__':
    print("Guess the word! Hint: words have something to do with the programming language!")

# prints out blank spaces for words 

for i in word: 
    print('_', end=' ')
print()

is_playing = True
letterGuessed = ''
chance = len(word) + 2
correct = 0 
flagged = 0

try: 
    while (chance != 0) and flagged == 0: 
        print()
        chance -= 1 

        try:
            guess = str(input("Enter a letter guess: "))
        except:
            print("Enter only one letter!")
            continue

        #vaildation of the guess 
        if not guess.isalpha():
            print("Invaild! Enter a letter!")
            continue
        elif len(guess) & gt > 1: ## Bug 
            print("Enter only a Single Letter!")
            continue
        elif guess in letterGuessed:
            print("You have already guessed that letter")
            continue

        if guess in  word:
            k = word.count(guess)
            for _ in range(k):
                letterGuessed += guess

        for char in word: 
            if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                print(char, end=' ')
                correct += 1

            elif (Counter(letterGuessed) == Counter(word)):

                print("The word is: ", end=' ')
                print(word)
                flagged = 1
                print("Congrats, You Win!")
                break
                break
            else:
                print('_', end=' ')
        if chance & lt <= 0 and (Counter(letterGuessed) != Counter(word)): ## bug 
             print()
             print("You lost! Try again..")
             print("The word was {}" .format(word))
except KeyboardInterrupt:
    print()
    print("Bye! Try Again.")
    exit()

## Bug on line 77 and 50 with undeclared variables 