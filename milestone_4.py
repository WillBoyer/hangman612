import random

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
        
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            # Finds which letters in word match the correct guess
            # Then reveals the letters in word_guessed
            guessed_index = [i for i in range(len(self.word)) if self.word[i] == guess]
            for i in guessed_index:
                self.word_guessed[i] = self.word[i]
            self.num_letters = self.num_letters - 1
            str_word_guessed = ''.join(self.word_guessed)
            print(f"Your answer so far: {str_word_guessed}")
        else:
            self.num_lives = self.num_lives - 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")
            
    def ask_for_input(self):
        is_valid = False
        while(not is_valid):
            guess = input("Guess a letter.\n")
            if len(guess) != 1 and guess.isalpha()==False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                is_valid = True