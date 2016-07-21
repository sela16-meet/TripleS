from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def welcome():
 	return render_template("welcome.html")

@app.route('/signin')
def signin():
 	return render_template("signin.html")

def go_to_sign_in():
	return render_template("signin.html")

@app.route('/signup')
def signup():
 	return render_template("signup.html")

@app.route('/contact')
def contact():
	return render_template("contact.html")

@app.route('/home')
def home():
	return render_template("home.html")

@app.route('/story')
def story():
	return render_template("story.html")

if __name__=="__main__":
 	app.run()