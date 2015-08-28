from app import app
#from app.forms import SignupForm
from flask import render_template

@app.route('/')
def index():
	return render_template('index.html')