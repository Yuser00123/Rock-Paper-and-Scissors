from flask import Flask, render_template, request
import game

app = Flask(__name__)
user_score = 0
ai_score = 0
tie_round = 0

user_move_count = {
    "rock": 0,
    "paper": 0,
    "scissors": 0
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def play():
    user_move = request.form.get('move').lower().strip()

    if user_move == "quit":
        return render_template('quit.html', user_score=user_score, ai_score=ai_score, tie_round=tie_round)
    elif user_move not in game.moves:
        return "alert('Invalid move. Please enter the correct move...')"
    else:
        user_move_count[user_move] += 1
        ai_move = game.get_ai_move(user_move_count)
        if user_move == ai_move:
            tie_round += 1
            return f"alert('It is a tie! Both chose {user_move}.')"
        elif game.beat[user_move] == ai_move:
            user_score += 1
            return f"alert('You win! Your move: {user_move} beats AI move: {ai_move}.')"
        else:
            ai_score += 1
            return f"alert('You lose! AI move: {ai_move} beats Your move: {user_move}.)"
    

if __name__ == '__main__':
    app.run(debug=True)