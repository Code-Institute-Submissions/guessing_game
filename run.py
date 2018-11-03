from flask import Flask, render_template, request, session
import random

app = Flask(__name__)

app.secret_key = 'secret'

@app.route("/")
def index():
	return render_template("index.html", user = "")

@app.route("/", methods = ["POST", "GET"])
def user_display():
	array = ("DOG", "CAT")
	current = random.choice(array)
	current_hidden = "?" * len(current)
	session["current"] = current
	session["current_hidden"] = current_hidden
	user = request.form["new_user"]
	user_greeting = "Welcome " + request.form["new_user"] + "!"
	session["user_greeting"] = user_greeting
	session["user"] = user
	return render_template("game.html", user_greeting = user_greeting, current = current_hidden)

@app.route("/guess/", methods=['POST', "GET"])
def guess():
	guess = request.form["guess"]
	guess = guess.upper()
	used = guess
	current_hidden = session.get("current_hidden")
	current = session.get("current")
	if guess in current:
		new_hidden = ""
		for x in range(len(current)):
			if guess == current[x]:
				new_hidden += guess
			else:
				new_hidden += current_hidden[x]              
		current_hidden = new_hidden
		session["current_hidden"] = current_hidden
		return render_template("game.html", guess = guess, current = current_hidden, user_greeting = "CORRECT!")
	else:
		return render_template("game.html", guess = guess, current = current_hidden, user_greeting = "WRONG!")
