from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("do_you_wanna.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def show_madlib_form():

    choice = request.args.get("game_choice")
    person = request.args.get("person")

    if choice == "no":
        return render_template("goodbye.html",
                           person=person)
    elif choice == "yes":
        return render_template("game.html",
                            person=person)
    else:
        pass

@app.route('/madlib')
def show_madlib():
    
    celebrity = request.args.get("celebrity")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    adverbs = request.args.getlist("adverbs")



    return render_template("madlib.html",
                           celebrity=celebrity,
                           color=color,
                           noun=noun,
                           adjective=adjective,
                           adverbs=adverbs)







if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
