import random

from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'


@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    return f'How did you know I liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun):
    return f'The {adjective} {noun} was having a difficult time creating this message'

@app.route('/multiply/<num1>/<num2>')
def multiply(num1, num2):
    if num1.isdigit() == True and num2.isdigit() == True:
        return f'{num1} * {num2} = {int(num1) * int(num2)}'
    else:
        return f'Invalid inputs. Please try again by entering 2 numbers!'

@app.route('/sayntimes/<word>/<num>')
def sayntimes(word, num):
    if num.isdigit() == True:
        sentence = ""
        for x in range(int(num)):
            sentence = f'{sentence} {word}'
        return sentence
    else:
        return f'Invalid inputs. Please try entering the word, then the number.'


@app.route('/dicegame/')
def dicegame():
    num = random.randint(1,6)
    if num < 6:
        return f'You rolled {num}, you lost'
    else:
        return f'You rolled {num}, you won!'
     

if __name__ == '__main__':
    app.run(debug=True)

