import random

moves = ['rock', 'paper', 'scissors']

def determine_winner(user, ai):
    if user == moves[ai]:
        print(f"AI choosed {moves[ai]}.")
        print("It is a tie between you and ai...")
    elif (user == 'rock' and ai == 1):
        print(f"AI choosed {moves[ai]}.")
        print("You lose! Paper beats rock...")
    elif (user == 'paper' and ai == 2):
        print(f"AI choosed {moves[ai]}.")
        print("You lose! Scissors beats paper...")
    elif (user == 'scissors' and ai == 1):
        print(f"AI choosed {moves[ai]}.")
        print("You win! Scissors beats paper...")
    elif (user == 'rock' and ai == 2):
        print(f"AI choosed {moves[ai]}.")
        print("You win! Rock beats scissors...")
    elif (user == 'paper' and ai == 0):
        print(f"AI choosed {moves[ai]}.")
        print("You win! Paper beats rock...")
    elif (user == 'scissors' and ai == 0):
        print(f"AI choosed {moves[ai]}.")
        print("You lose! Rock beats scissors...")
    else:
        print("Invalid input. Please enter rock, paper, or scissors.")

playing = True

while playing:
    user_move = input("Enter your move (rock, paper scissors): ").lower()
    ai_move = random.randint(0, 2)
    if user_move == 'q':
        print("Thanks for playing!")
        playing = False
    else:
        determine_winner(user_move, ai_move)



