"""
        Number Guesser Game 
        Ask user if they want to play. 
        Start the game:
        Limit the number by the range the user 1 to top number user provides.
        Keep quesses count.  

        Generate random number 
        Take inputs and check if user guesses the random number.
        Confirm if guess is: less than or greater than the random number.
        Return number of guesses it took to guess the number.
        Ask if they want to play again.
"""
import random 
print('Number Guessing Game')
print(You choose the largest number the random number could be, then guess it!')

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
    
    top_of_range = input('Input a Number: ')
    if top_of_range.isdigit() :
       top_of_range = int(top_of_range)
       if top_of_range <= 1 :
          print('Please type a number higher than 1')
          start_game()
    else: 
       print('Please type a number next time.')
       start_game()

    random_number = random.randint(1, top_of_range)
    guesses = 0

    while True :
            guesses += 1
            user_guess = input('Guess the number: ')
            if user_guess.isdigit() :
                user_guess = int(user_guess)
            else :
                print('Please type a number next time.')
                continue
            
            if user_guess == random_number :
                print('You guessed it!')
                break
            elif user_guess > random_number :
                print('Your guess is greater than the number. 😏')
            else :
                print('Your guess is less than the number. 😏')

    print(' 🤩 Success! you guessed the number in ', guesses, 'guesses!')
    start_game()
            
start_game()





