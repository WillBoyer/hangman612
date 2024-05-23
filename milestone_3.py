def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print("Good guess! {guess} is in the word.")
    else:
        print("Sorry, {guess} is not in the word. Try again.")
    
    
def ask_for_input():
    while(True):
        guess = input("Guess a letter.")
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)