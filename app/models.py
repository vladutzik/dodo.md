from app import db
from datetime import datetime

class Event(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(255))
	content = db.Column(db.Text)
	start_date = db.Column(db.DateTime)
	end_date = db.Column(db.DateTime)
	organizer = db.Column(db.String(255))
	published_at = db.Column(db.DateTime, default=datetime.utcnow)
	price = db.Column(db.Integer)
	# photo = db.Column(db.String(255))
	additional_info = db.Column(db.Text)
	target_group = db.Column(db.Text)
	location = db.Column(db.Text)
	phone = db.Column(db.Integer)
	email = db.Column(db.String(50))
	
	category_id =  db.Column(db.Integer, db.ForeignKey('category.id') ) 
	category = db.relationship('Category', 
		backref = db.backref('posts', lazy = 'dynamic'))
	
	district_id = db.Column(db.Integer, db.ForeignKey('district.id') ) 
	district =  db.relationship('District', 
		backref = db.backref('posts', lazy = 'dynamic'))
	
	type_event_id = db.Column(db.Integer, db.ForeignKey('type.id') ) 
	type_event =  db.relationship('Type', 
		backref = db.backref('posts', lazy = 'dynamic'))

	# def __init__(title, content, start_date, end_date, organizer, published_at,
	# 	price, phone, additional_info, target_group, location, photo, email)


class Category(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(255))
	
class District(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(255))

class Type(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(255))	

class EventImage(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	event_id = db.Column(db.Integer, db.ForeignKey('event.id') )
	event = db.relationship('Event', 
		backref = db.backref('images', lazy = 'dynamic'))
	image_link= db.Column(db.Text)

	def __str__(self):
		return 'event_id: {}, image_link: {}'.format(self.event_id, self.image_link)

		