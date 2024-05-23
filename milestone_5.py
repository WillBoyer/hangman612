from milestone_4 import Hangman

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    finished = False
    while(not finished):
        game.ask_for_input()
        if game.num_lives == 0:
            print("You lost!")
            finished = True
        elif game.num_letters > 0:
            print(f"There are {game.num_letters} letters left to guess")
        else:
            print("Congratulations. You won the game!")
            finished = True
        
        
play_game(['apple', 'banana', 'apricot', 'pineapple', 'tomato'])