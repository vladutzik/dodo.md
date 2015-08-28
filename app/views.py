from app import app, db
from forms import SignupForm
from forms import EventForm, AddCategoryForm
from flask import render_template, request
from models import Category

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	form = SignupForm()
	if form.validate_on_submit():
		print "nume:",form.nume.data, "prenume:", form.prenume.data, "parola:", form.parola.data
		return render_template('index.html')
	return render_template('signup.html',form=form) 

@app.route('/event')
def event():
	form = EventForm()
	return render_template('create_event.html', form=form)

@app.route('/category/add',methods=['GET', 'POST'])
def add_category():
	form = AddCategoryForm()
	if request.method == 'POST' :
		category = Category(form.name.data)
		db.session.add(category)
		db.session.commit()
		return render_template('index.html')
	return render_template('add_category.html',form=form)