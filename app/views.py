from app import app, db
from forms import SignupForm, EventForm, SigninForm, EventForm, AddImageToEvent, AddCategoryForm
from flask import render_template, request, redirect
from models import Event, TargetGroup, TypeEvent, Category, District, EventImage, Category, Users
from datetime import datetime


@app.route('/signup', methods=['GET','POST'])
def signup():
	form = SignupForm(request.form, csrf_enabled=True)
	print request.method
	if request.method == 'POST':
		print form.type_id.data
		print "method POST - save data to database"
		print unicode(form.type_id)
		users = Users(nume = form.nume.data, 
							email = form.email.data,
							parola = form.parola.data)
		db.session.add(users)
		db.session.commit()
		return render_template("index.html", form=form)
	return render_template("signup.html", form=form)


@app.route('/event', methods=['GET','POST'])
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
		print unicode(form.district_id)
		form_tasks = Event(titlu = form.titlu.data, 
		start_date = form.start_date.data,
		end_date = form.end_date.data,
		organizers = form.organizers.data,
		price = form.price.data,
		photo = form.photo.data,
		additional_info = form.additional_info.data,
		location = unicode(form.location.data),
		target_group_id = target_group.id,
		type_event_id = type_event.id,
		category_id = category.id,
		district_id = district.id)
		# form.populate_obj(form_tasks)
		db.session.add(form_tasks)
		db.session.commit()
		return render_template("index.html", form=form)
	return render_template("event.html", form=form)


@app.route('/')
def index():
	event = Event.query.get(2)
	animals_list = ['Enot', 'Elefant', 'Enot2', 'Zebra']
	today = datetime.now()
	new_day = today.day
	print "index"
	return render_template("index.html", day = new_day, animals = animals_list, best_animal = "Mark", event = event)

@app.route('/register', methods = ['GET', 'POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		print form.nume.data, form.parola.data
		return render_template("index_dodo.html")
	return render_template("signup.html", form = form)

@app.route('/showevent/<int:event_id>', methods = ['GET', 'POST'])
def show_event(event_id):
	# event_title = Event.query.filter_by(title=title).first_or_404()
	event = Event.query.get(event_id)
	 # print event, event_id
	print event
	return render_template("show_event.html", event = event)

@app.route('/listevents', methods = ['GET', 'POST'])
def list_events():
	# for event_id in
	#event_title = Event.query.filter_by(title=title).first_or_404()
	events = Event.query.all()
	 # print event, event_id
	print events
	return render_template("list_events.html", events = events)


@app.route('/signin', methods = ['POST', 'GET'])
def signin():
	form = SigninForm()
	if form.validate_on_submit():
		print form.nume.data, form.parola.data
		return render_template("index_dodo.html")
	return render_template("signin.html", form = form)


# def addImageToEvent(id_event, img_link):
# 	event_img = EventImage(event_id = id_event, image_link = img_link) 
# 	db.session.add(me)
# 	db.session.commit()

@app.route('/event/<int:event_id>', methods = ['GET', 'POST'])
def addImageToEvent(event_id):
	form = AddImageToEvent(request.form, csrf_enabled=True)
	if request.method == 'POST':
		event_img = EventImage(event_id=event_id, image_link=form.image_link.data)
		print "!!!imglink:" + form.image_link.data
		db.session.add(event_img)
		db.session.commit()
		return redirect("showevent/{}".format(event_id))
	return render_template("add_images.html", form = form, event_id = event_id)

@app.route('/date')
def date():
	today = datetime.now()
	return "Azi este " + str(today.day) + "." + str(today.month) + "." +\
	 str(today.year) + ", ora " + str(today.hour) + ":" + str(today.minute) + ":" + str(today.second)

@app.route('/user/<name>')
def user(name):
	return 'Hello ' + str(name) + "!!!"


@app.route('/categories')
def categories():
	return render_template('/categories.html')

@app.route('/contact_us')
def contact_us():
	# form = ContactUsForm()
	# if form.validate_on_submit():
	# 	print form.email.data, form.message.data
	# 	return render_template("index_dodo.html")
	return render_template('/contact_us.html')


@app.route('/category/add',methods=['GET', 'POST'])
def add_category():
	form = AddCategoryForm()
	if request.method == 'POST' :
		category = Category(form.name.data)
		db.session.add(category)
		db.session.commit()
		return render_template('index.html')
	return render_template('add_category.html',form=form)
