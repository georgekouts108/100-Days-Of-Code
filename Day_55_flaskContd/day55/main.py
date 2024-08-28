from flask import Flask, render_template
import random

app = Flask(__name__)

ANSWER = random.randint(1, 10)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/<guess>')
def guess_number(guess):
    try:
        guess = int(guess)
        if guess not in [i for i in range(1, 11)]:
            raise Exception()

        if guess == ANSWER:
            return render_template('correct.html')
        elif guess < ANSWER:
            return render_template('too_low.html')
        elif guess > ANSWER:
            return render_template('too_high.html')

    except Exception:
        return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
