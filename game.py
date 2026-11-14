import random

moves = ["rock", "paper", "scissors"]

beat = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

def get_ai_move():
    ai_move = moves[random.randint(0, 2)]
    return ai_move

def main():
    print("Welcome to Rock, Paperand Scissors game!")
    
    while True:
        user_move = input("Enter your move (rock, paper, scissors) or q to quit: ")

        if user_move == "q":
            print("Thanks for playing! Byeee...")
            break

        if user_move not in moves:
            print("Invalid move. Please type correct move...")
            continue

        ai_move = get_ai_move()
        print(f"AI chose: {ai_move} \nYou chose: {user_move}")

        if user_move == ai_move:
            print("It is a tie!")
        elif beat[user_move] == ai_move:
            print(f"You win! {user_move} beats {ai_move}.")
        else:
            print(f"You loose! {ai_move} beats {user_move}.")

if __name__ == "__main__":
    main()
