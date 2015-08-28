from app import db

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
	__tablename__='evenimente'
	id = db.Column(db.Integer, primary_key=True)
	titlu = db.Column(db.String(255))
	start_date = db.Column(db.DateTime)
	end_date = db.Column(db.DateTime, nullable=True)
	organizers = db.Column(db.String(255))
	published_at = db.Column(db.DateTime)
	price = db.Column(db.Integer,nullable=True)
	location = db.Column(db.Text)
	photo = db.Column(db.String(255),nullable=True)
	additional_info = db.Column(db.Text,nullable=True)
	
	district_id = db.Column(db.Integer, db.ForeignKey('districts.id'))
	district = db.relationship('District', 
		backref=db.backref('evenimente', lazy='dynamic', order_by= id))

	
	category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
	category = db.relationship('Category', 
		backref=db.backref('evenimente', lazy='dynamic', order_by = id))
	phone = db.Column(db.Integer)

	type_event_id = db.Column(db.Integer, db.ForeignKey('typeevent.id'))
	type_event = db.relationship('TypeEvent', 
		backref=db.backref('evenimente', lazy='dynamic',order_by= id))
	phone = db.Column(db.Integer)

	target_group_id = db.Column(db.Integer, db.ForeignKey('targetgroup.id'))
	target_group = db.relationship('TargetGroup', 
		backref=db.backref('evenimente', lazy='dynamic',order_by= id))
	phone = db.Column(db.Integer)

class UserType(db.Model):
	__tablename__='user_types'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))

class Users(db.Model):
	__tablename__='users'
	id = db.Column(db.Integer, primary_key=True)
	nume = db.Column(db.String(255))
	email = db.Column(db.String(40))
	parola = db.Column(db.String(20))

	user_type_id = db.Column(db.Integer, db.ForeignKey('user_types.id'))
	user_type = db.relationship('UserType', 
		backref=db.backref('users', lazy='dynamic',order_by= id))
	phone = db.Column(db.Integer)
		