from app import app
from app import db
from datetime import datetime
from flask import render_template, request, redirect
from app.forms import SigninForm, EventForm, AddImageToEvent
from app.models import Event, EventImage

@app.route('/')
def index():
	animals_list = ['Enot', 'Elefant', 'Enot2', 'Zebra']
	today = datetime.now()
	new_day = today.day
	print "index"
	return render_template("index.html", day = new_day, animals = animals_list, best_animal = "Mark")

@app.route('/register', methods = ['GET', 'POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		print form.nume.data, form.parola.data
		return render_template("index_dodo.html")
	return render_template("register.html", form = form)

@app.route('/showevent/<int:event_id>', methods = ['GET', 'POST'])
def show_event(event_id):
	# event_title = Event.query.filter_by(title=title).first_or_404()
	event = Event.query.get(event_id)
	 # print event, event_id
	print event
	return render_template("show_event.html", event = event)


@app.route('/signin', methods = ['POST', 'GET'])
def signin():
	form = SigninForm()
	if form.validate_on_submit():
		print form.nume.data, form.parola.data
		return render_template("index_dodo.html")
	return render_template("signin.html", form = form)


@app.route('/event', methods = ['GET', 'POST'])
def event():
	form = EventForm(request.form, csrf_enabled=True)
	print request.method
	print datetime.utcnow()
	print form.photo.data
	if request.method == 'POST':
		print "method POST - save data to database"
		event = Event(title = form.title.data,
		content = form.content.data,
		start_date = form.start_date.data, 
		end_date = form.end_date.data, 
		organizer = form.organizer.data, 
		price = form.price.data,
		additional_info = form.additional_info.data,
		target_group = form.target_group.data,
		location = form.location.data,
		phone = form.phone.data,
		email = form.email.data,
	# !!!!!!! ids!!!
		# # category_id = form.category_id.data,
		# category = form.category.data,
		# # district_id = form.district_id.data,
		# district = form.district.data,
		# # type_event_id = form.type_event_id.data,
		# type_event = form.type_event.data
		)
		db.session.add(event)
		db.session.commit()
		event_img = EventImage(event_id=event.id, image_link=form.photo.data)
		db.session.add(event_img)
		db.session.commit()
		# form.populate_obj(event)
		return redirect("event/{}".format(event.id))
	return render_template("event.html", form = form)

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

