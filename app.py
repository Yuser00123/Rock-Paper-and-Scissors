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
    print(f"AI chose {ai_move}.")
    if result == "tie":
        print("It's a tie!")
    elif result == "lose":
        print(f"You lose! {ai_move} beats {user_move}.")
    else:
        print(f"You won! {user_move} beats {ai_move}")
    return result



def main():
    print("Welcome to rock paper and scissors!") 
    user_score = 0
    ai_score = 0
    ties = 0
    while True:
        user_move = input("\nYour move (rock, paper, scissors - q to quit): ").strip().lower()
        if user_move == "q":
            if user_score > ai_score:
                print(f"Your final score is {user_score} and the AI's score is {ai_score} and tie rounds are {ties}. You won!")
            elif user_score < ai_score:
                print(f"Your final score is {user_score} and the AI's score is {ai_score} and tie rounds are {ties}. You lost!")
            else:
                print(f"Your final score is {user_score} and the AI's score is {ai_score} and tie rounds are {ties}. It's a tie!")
            print("byeeee!")
            break
        if user_move not in moves:
            print("Please enter a valid move.")
            continue 

        result = play_round(user_move)
        if result == "win":
            user_score += 1
        elif result == "lose":
            ai_score += 1
        else:
            ties += 1

if __name__ == "__main__":
    main()





