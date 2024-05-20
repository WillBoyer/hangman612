import random


word_list = ['apple', 'banana', 'apricot', 'pineapple', 'tomato']
print(word_list)
word = random.choice(word_list)
print(word)
guess = input("Guess the first letter.")
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! that is not a valid input.")