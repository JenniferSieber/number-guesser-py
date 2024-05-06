"""
Number Guesser Game in 3 or less guesses
Limit the number between 1 - 10
Keep score.  
correct answer on guess: guesscount  - numOfGuesses + 1 for score..

Ask number of times want to play.
Generate random number 
Take inputs and check if user guesses the random number.
"""
import random 
print('Number Guessing Game')
print('Within 3 Guesses, Guess the Number the computer generated randomly between 1 and 10')

def start_game() :
    print()
    play = input('Do you want to play a game --yes or no?  ').lower()
    if play == 'yes' :
        print("Let's Play! 🥳")
        game_play(6)

    elif play != 'yes' :
      print('  😔 Maybe another time.')
      quit()

def game_play(game_len) :
    score = 5
    answer = random.randint(1, 10)
    winner = False
    # print(answer, 'answer') # use for testing
    
    for i, num in enumerate(range(1, game_len)) :
        print('Guess: ', num, 'Score: ', score)
        user_guess = input('Whats your number guess between 1 - 10?  ')
        user_guess = int(user_guess)
        print('Your guess: ', user_guess)
        if user_guess == answer :
            winner = True
            break
        else :
            score -= 1
            
    if winner == True :
        print(' 🤩  You Win! Your score is: ', score)
        start_game()
    else :
        print(' 😏  You Lose. The winning answer was: ', answer)
        start_game()

    winner = False

start_game()






