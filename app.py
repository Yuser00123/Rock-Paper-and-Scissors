import os
from datetime import timedelta

from flask import Flask, render_template, request, session
import game

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-change-me")
app.permanent_session_lifetime = timedelta(days=30)


def initialize_session():
    session.permanent = True
    session.setdefault("user_score", 0)
    session.setdefault("ai_score", 0)
    session.setdefault("tie_round", 0)
    session.setdefault("user_move_count", {
        "rock": 0,
        "paper": 0,
        "scissors": 0
    })

@app.route('/')
def home():
    initialize_session()
    return render_template(
        'index.html',
        user_score=session["user_score"],
        ai_score=session["ai_score"],
        tie_round=session["tie_round"]
    )

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/submit', methods=['POST'])
def play():
    initialize_session()
    user_move = request.form.get('move', '').lower().strip()

    if user_move == "quit":
        return render_template(
            'quit.html',
            user_score=session["user_score"],
            ai_score=session["ai_score"],
            tie_round=session["tie_round"]
        )
    elif user_move not in game.moves:
        return render_template('invalid.html', user_move=user_move)
    else:
        user_move_count = session["user_move_count"]
        ai_move = game.get_ai_move(user_move_count)
        user_move_count[user_move] += 1
        session["user_move_count"] = user_move_count

        if user_move == ai_move:
            session["tie_round"] = session["tie_round"] + 1
            return render_template('tie.html', user_move=user_move)
        elif game.beat[user_move] == ai_move:
            session["user_score"] = session["user_score"] + 1
            return render_template('win.html', user_move=user_move, ai_move=ai_move)
        else:
            session["ai_score"] = session["ai_score"] + 1
            return render_template('lose.html', user_move=user_move, ai_move=ai_move)
    
@app.route('/certificate')
def certificate():
    return render_template('certificate.html')

if __name__ == '__main__':
    app.run(debug=True)