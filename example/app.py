from flask import Flask, render_template
from flaskext.autoversion import Autoversion

app = Flask(__name__)
app.autoversion = True
av = Autoversion(app)

@app.route('/')
def hello_world():
	return render_template("home.html")

if __name__ == "__main__":
	app.run()