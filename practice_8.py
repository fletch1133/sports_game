import random
import sys
from termcolor import colored
import nltk
nltk.download('words')
from nltk.corpus import words



def print_menu():
    print("Let's play Wordle:")
    print("Type a 5 letter word and hit enter!\n") 


# def nltk_rand_word():
#     pass 
 
def read_rand_word():
    with open("words.txt") as f:
        word_lines = f.read().splitlines() 
        return random.choice(word_lines) 
    

nltk.data.path.append('/work/words') 
word_list = words.words()
words_five = [word for word in word_list if len(word) == 5]

print_menu() 
play_again = ""
while play_again != "q":
    # word = read_rand_word()
    word = random.choice(words_five) 

    for attempt in range(1, 7): 
        guess  = input().lower()

        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K') 
        
        for attempt in range( min(len(guess), 5) ):
            if guess[attempt] == word[attempt]: 
                print(colored(guess[attempt], 'green'), end="") 
            elif guess[attempt] in word:
                print(colored(guess[attempt], 'yellow'), end="")
            else:
                print(guess[attempt], end="")
        print()

        if guess == word:
            print(colored(f"Congrats! You got the wordle in {attempt} attempts", 'red'))
            break
        elif attempt == 6: 
            print("Sorry, the wordle was... {word}") 

    play_again = input("Want to play again? Type q to exit.") 