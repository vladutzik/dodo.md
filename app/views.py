from app import app
from app import db
from forms import SignupForm, EventForm
from flask import render_template, request
from app.models import Event, TargetGroup, TypeEvent, Category, District

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
	form = SignupForm(request.form, csrf_enabled=True)
	print request.method
	if request.method == 'POST':
		print form.type_id.data
		print "method POST - save data to database"
		print unicode(form.type_id)
		form_tasks = Signup(nume = form.nume.data, 
							email = form.email.data,
							parola = form.parola.data)
		db.session.add(form_tasks)
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
		published_at = form.published_at.data,
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

			

