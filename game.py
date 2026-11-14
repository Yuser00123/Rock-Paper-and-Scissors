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
    print("Welcome to Rock, Paper and Scissors game!")
    user_score = 0
    ai_score = 0
    tie_rounds = 0
    while True:
        user_move = input("Enter your move (rock, paper, scissors) or q to quit: ").lower().strip()

        if user_move == "q":
            print("\nStatistics:")
            print(f"\nYou scored {user_score} points.")
            print(f"AI scored {ai_score} points.")
            print(f"Total tie rounds played are {tie_rounds}.")
            if user_score > ai_score:
                print("Congratulations! You won the game.")
            elif user_score < ai_score:
                print("You lost the game! Better luck next time.")
            else:
                print("The game ends in a tie.")
            print("Thanks for playing! Byeee...")
            break

        if user_move not in moves:
            print("Invalid move. Please type correct move...")
            continue

        ai_move = get_ai_move()
        print(f"AI chose: {ai_move} \nYou chose: {user_move}")

        if user_move == ai_move:
            print("It is a tie!")
            tie_rounds += 1
        elif beat[user_move] == ai_move:
            print(f"You win! {user_move} beats {ai_move}.")
            user_score += 1
        else:
            print(f"You loose! {ai_move} beats {user_move}.")
            ai_score += 1


if __name__ == "__main__":
    main()
