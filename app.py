import random

moves = ['rock', 'paper', 'scissors']
user_score = 0
ai_score = 0

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
    global user_score, ai_score
    result = determine_winner(user_move, ai_move)
    print(f"AI chose {ai_move}.")
    if result == "tie":
        print("It's a tie!")
    elif result == "lose":
        print(f"You lose! {ai_move} beats {user_move}.")
        ai_score += 1
    else:
        print(f"You won! {user_move} beats {ai_move}")
        user_score += 1



def main():
    print("Welcome to rock paper and scissors!") 
    while True:
        user_move = input("\nYour move (rock, paper, scissors - q to quit): ").strip().lower()
        if user_move == "q":
            if user_score > ai_score:
                print(f"Your final score is {user_score} and the AI's score is {ai_score}. You won!")
            elif user_score < ai_score:
                print(f"Your final score is {user_score} and the AI's score is {ai_score}. You lost!")
            else:
                print(f"Your final score is {user_score} and the AI's score is {ai_score}. It's a tie!")
            print("byeeee!")
            break
        if user_move not in moves:
            print("Please enter a valid move.")
            continue 

        play_round(user_move)

if __name__ == "__main__":
    main()





