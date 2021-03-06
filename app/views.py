# -*- coding: utf-8 -*-
from app import app, db
from app import login_manager
from forms import SignupForm, EventForm, AddImageToEvent, SigninForm, ContactUsForm
from flask import render_template, request, redirect
from app.models import Event, TargetGroup, TypeEvent, Category, District, EventImage, Users
from datetime import datetime
from flask.ext.login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash


@login_manager.user_loader
def load_user(userid):
	user = Users.query.get(userid)
	return user

@app.route('/', methods = ['GET', 'POST'])
def index():
	events = Event.query.all()
	for e in events:
		print e
	imag = ['https://pbs.twimg.com/profile_images/378800000532546226/dbe5f0727b69487016ffd67a6689e75a.jpeg',
	'https://pbs.twimg.com/profile_images/378800000532546226/dbe5f0727b69487016ffd67a6689e75a.jpeg',
	 'https://stuchambers.files.wordpress.com/2012/08/training-course-group.jpg',
	  'http://www.uni-regensburg.de/international/austausch-programmstudierende/medien/image_studieren_ar__1_.jpeg',
	  'https://pbs.twimg.com/profile_images/378800000532546226/dbe5f0727b69487016ffd67a6689e75a.jpeg',
	  'https://pbs.twimg.com/profile_images/378800000532546226/dbe5f0727b69487016ffd67a6689e75a.jpeg',
	  'https://pbs.twimg.com/profile_images/378800000532546226/dbe5f0727b69487016ffd67a6689e75a.jpeg']
	return render_template("index.html", events = events, imag=imag)

@app.route('/signup', methods=['GET','POST'])
def signup():
	form = SignupForm(request.form, csrf_enabled=True)
	print request.method
	if request.method == 'POST':

		user_type = form.user_type_id.data
		
		print "method POST - save data to database"
		print form.parola.data
		form_tasks = Users(nume = form.nume.data, 
							email = form.email.data,
							parola = generate_password_hash(form.parola.data),
							user_type= form.user_type_id.data)
		db.session.add(form_tasks)
		db.session.commit()
		return redirect('/')
	return render_template("signup.html", form=form)

@app.route('/event', methods=['GET','POST'])
@login_required
def event():
	form = EventForm(request.form, csrf_enabled=True)
	print request.method
	if request.method == 'POST':
		print form.target_group_id.data
		target_group = form.target_group_id.data
		type_event = form.type_event_id.data
		category = form.category_id.data
		district = form.district_id.data
		print target_group, type_event, category, district

		print "method POST - save data to database"
		# print form.district_id.enco  de('utf8')
		form_tasks = Event(titlu = form.titlu.data, 
		start_date = form.start_date.data,
		end_date = form.end_date.data,
		organizers = form.organizers.data,
		price = form.price.data,
		photo = form.photo.data,
		phone = form.phone.data,
		content = form.content.data,
		additional_info = form.additional_info.data,
		location = unicode(form.location.data),
		target_group_id = target_group.id,
		type_event_id = type_event.id,
		category_id = category.id,
		district_id = district.id)
		# form.populate_obj(form_tasks)
		db.session.add(form_tasks)
		db.session.commit()
		return redirect("/")
	return render_template("event.html", form=form)

@app.route('/register', methods = ['GET', 'POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		print form.nume.data, form.parola.data
		return render_template("index.html", event)
	return render_template("signup.html", form = form)

@app.route('/showevent/<int:event_id>', methods = ['GET', 'POST'])
def show_event(event_id):
	# event_title = Event.query.filter_by(title=title).first_or_404()
	event = Event.query.get(event_id)
	 # print event, event_id
	if request.method == "POST":
		return redirect("/deleteevent/{}".format(event_id))
	print event
	return render_template("show_event.html", event = event)


@app.route('/deleteevent/<int:event_id>', methods = ['GET', 'POST'])
def delete_event(event_id):
	# event_title = Event.query.filter_by(title=title).first_or_404()
	event = Event.query.get(event_id)
	if request.method == 'POST':
		db.session.delete(event)
		db.session.commit()	
		return redirect('/')
	print event
	return render_template("delete.html", event = event)


@app.route('/list_all_events', methods = ['GET', 'POST'])
def list_all_events():
	# for event_id in
	#event_title = Event.query.filter_by(title=title).first_or_404()
	events = Event.query.all()
	for e in events:
		print e
	 # print event, event_id
	print events
	return render_template("list_all_events.html", events = events)

@app.route('/list_category_events/<int:category_id>', methods = ['GET', 'POST'])
def list_category_events(category_id):
	# for event_id in
	#event_title = Event.query.filter_by(title=title).first_or_404()
	events = Event.query.filter_by(category_id=category_id).all()
	category = Category.query.get(category_id)
	for e in events:
		print e
	 # print event, event_id
	print events
	return render_template("list_category_events.html", events = events, category=category)


@app.route('/signin', methods = ['POST', 'GET'])
def signin():
	form = SignupForm()
	error = ''
	if form.validate_on_submit():
		print '************'
		print form.email.data, form.parola.data
		parola = generate_password_hash(form.parola.data)
		print parola
		users = Users.query.filter_by(email=form.email.data).all()
		print "########"
		for user in users:
			print user.parola
			if check_password_hash(user.parola, form.parola.data):
				login_user(user)
				print 'logged in successfully'
				return redirect('/')
				break
		error = "login usuccesful"
		print error
	return render_template("signup.html", form = form, error=error)

@app.route('/event/<int:event_id>', methods = ['GET', 'POST'])
@login_required
def addImageToEvent(event_id):
	form = AddImageToEvent(request.form, csrf_enabled=True)
	if request.method == 'POST':
		event_img = EventImage(event_id=event_id, image_link=form.image_link.data)
		print "!!!imglink:" + form.image_link.data
		db.session.add(event_img)
		db.session.commit()
		return redirect("showevent/{}".format(event_id))
	return render_template("add_images.html", form = form, event_id = event_id)


@app.route('/categories')
def categories():
	categories = Category.query.all()
	color = ['red', 'green', 'blue', 'yellow']
	return render_template('/categories.html', categories=categories, color=color)

@app.route('/contact_us')
def contact_us():
	form = ContactUsForm()
	if form.validate_on_submit():
		print form.email.data, form.message.data
	 	return redirect("/")
	return render_template('/contact_us.html')

@app.route('/about_us')
def about_us():
	return render_template('/about_us.html')


@app.route('/category/add',methods=['GET', 'POST'])
@login_required
def add_category():
	form = AddCategoryForm()
	if request.method == 'POST' :
		category = Category(form.name.data)
		db.session.add(category)
		db.session.commit()
		return redirect('/')
	return render_template('add_category.html',form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')

@app.route('/construction')
def construction():
	return render_template('/construction.html')
