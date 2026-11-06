import random

moves = ['rock', 'paper', 'scissors']

beats = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors':'paper'
}

def determine_winner(user_move, ai_move):
    if (user_move == ai_move):
        return "tie"
    if beats[user_move] == ai_move:
        return "win"
    return "lose"

def play_round(user_move):
    ai_move = moves[random.randint(0, 2)]
    result = determine_winner(user_move, ai_move)
    print(f"Ai chose {ai_move}.")
    if result == "tie":
        print("It's a tie!")
    elif result == "lose":
        print(f"You lose! {ai_move} beats {user_move}.")
    else:
        print(f"You won! {user_move} beats {ai_move}")



def main():
    print("Welcome to rock paper and scissors!") 

    while True:
        user_move = input("\nYour move (rock, paper, scissors - q to quit): ").strip().lower()
        if user_move == "q":
            print("byeeee!")
            break
        if user_move not in moves:
            print("Please enter a valid move.")
            continue 

        play_round(user_move)

if __name__ == "__main__":
    main()





