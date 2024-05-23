import random

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = set(self.word)
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
        
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index, letter in self.word:
                if letter == guess:
                    # Get corresponding blank in word_guessed
                    self.word_guessed[index] = letter
            num_letters -= 1
        else:
            num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")
            
    def ask_for_input(self):
        while(True):
            guess = input("Guess a letter.\n")
            if len(guess) != 1 and guess.isalpha()==False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break
            
            
hangman = Hangman(word_list=['apple', 'banana', 'apricot', 'pineapple', 'tomato'])
hangman.ask_for_input()