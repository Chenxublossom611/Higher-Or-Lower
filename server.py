from flask import Flask
import random
app = Flask(__name__)


@app.route('/')
def higher_or_lower():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/l2JJDdD7cv4xdGGis/giphy-downsized-large.gif'>"

random_number = random.randint(0,9)
print(random_number)

@app.route('/<int:number>')
def game(number):
    if number < random_number:
        return "<h1 style='color: yellow'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/kgHj1Jtzga4UO7DmLC/giphy.gif'>"
    if number > random_number:
        return "<h1 style='color: pink'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/8vQSQ3cNXuDGo/giphy.gif'>"
    if number == random_number:
        return "<h1 style='color: green'>You found me!<3</h1>" \
               "<img src='https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)