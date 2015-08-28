from app import app, db
# from forms import UserForm
from datetime import datetime
from flask import render_template, request
# from models import User
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/categories')
def categories():
	return render_template('/categories.html')

@app.route('/contact_us')
def contact_us():
	return render_template('/contact_us.html')
		
		# @app.route('/add_event', methods=['GET','POST'])
		# def add_event():
		# 	form=EventForm()
		# 	if request.method== 'POST':
		# 		title=form.title.data
		# 		content=form.content.data
		# 		start_date=form.start_date.data
		# 		db.session.add(eveniment)
		# 		db.session.commit()
		# 		eveniment=Eveniment(title, content, start_date)
		# 		return render_template('index.html')
		#  	return render_template('add_event.html', form=form)
		
	# 	 @app.route('/log_in',methods=['GET','POST'])
	# 	 def log_in():
	# 		form=UserForm()''
	# if request.method== 'POST':
	# 	name=form.name.data
	# 	password=form.password.data
	# 	email=form.email.data
	# 	type_id=form.type_id.data
	# 	db.session.add(user)
	# 	db.session.commit()
	# 	user=User(name, password, email, type_id)
	# 	return render_template('index.html')
 # 	return render_template('log_in.html', form=form)

