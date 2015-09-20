from werkzeug.security import generate_password_hash, \
     check_password_hash
from flask.ext.login import UserMixin
from app import db
from datetime import datetime

class Category(db.Model):
	__tablename__='categories'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))

class District(db.Model):
	__tablename__='districts'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50, convert_unicode=True))

class TypeEvent(db.Model):
	__tablename__='typeevent'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))

class TargetGroup(db.Model):
	__tablename__='targetgroup'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))

class Event(db.Model):
	__tablename__='events'
	id = db.Column(db.Integer, primary_key=True)
	titlu = db.Column(db.String(255))
	start_date = db.Column(db.DateTime)
	end_date = db.Column(db.DateTime, nullable=True)
	organizers = db.Column(db.String(255))
	published_at = db.Column(db.DateTime, default=datetime.utcnow)
	price = db.Column(db.Integer,nullable=True)
	location = db.Column(db.Text)
	photo = db.Column(db.String(255))
	additional_info = db.Column(db.Text,nullable=True)
	
	district_id = db.Column(db.Integer, db.ForeignKey('districts.id'))
	district = db.relationship('District', 
		backref=db.backref('events', lazy='dynamic', order_by= id))

	
	category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
	category = db.relationship('Category', 
		backref=db.backref('events', lazy='dynamic', order_by = id))
	phone = db.Column(db.Integer)

	type_event_id = db.Column(db.Integer, db.ForeignKey('typeevent.id'))
	type_event = db.relationship('TypeEvent', 
		backref=db.backref('events', lazy='dynamic',order_by= id))

	target_group_id = db.Column(db.Integer, db.ForeignKey('targetgroup.id'))
	target_group = db.relationship('TargetGroup', 
		backref=db.backref('events', lazy='dynamic',order_by= id))

class UserType(db.Model):
	__tablename__='user_types'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))

class Users(db.Model, UserMixin):
	__tablename__='users'
	id = db.Column(db.Integer, primary_key=True)
	nume = db.Column(db.String(255))
	email = db.Column(db.String(40))
	parola = db.Column(db.String(20))
	user_type_id = db.Column(db.Integer, db.ForeignKey('user_types.id'))
	user_type = db.relationship('UserType', 
		backref=db.backref('users', lazy='dynamic',order_by= id))


	def set_password(self, password):
		self.parola = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.pw_hash, password)

	def is_active(self):
		return True

class EventImage(db.Model):
	__tablename__='images'
	id = db.Column(db.Integer, primary_key = True)
	event_id = db.Column(db.Integer, db.ForeignKey('events.id') )
	event = db.relationship('Event', 
		backref = db.backref('images', lazy = 'dynamic'))
	image_link= db.Column(db.Text)

	def __str__(self):
		return 'event_id: {}, image_link: {}'.format(self.event_id, self.image_link)
