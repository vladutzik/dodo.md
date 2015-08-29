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
	__tablename__='events'
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
		backref=db.backref('events', lazy='dynamic', order_by= id))

	
	category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
	category = db.relationship('Category', 
		backref=db.backref('events', lazy='dynamic', order_by = id))
	phone = db.Column(db.Integer)

	type_event_id = db.Column(db.Integer, db.ForeignKey('typeevent.id'))
	type_event = db.relationship('TypeEvent', 
		backref=db.backref('events', lazy='dynamic',order_by= id))
	phone = db.Column(db.Integer)

	target_group_id = db.Column(db.Integer, db.ForeignKey('targetgroup.id'))
	target_group = db.relationship('TargetGroup', 
		backref=db.backref('events', lazy='dynamic',order_by= id))
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
	


# from datetime import datetime

# # class Eveniment(db.Model):
# # 	id=db.Column(db.Integer, primary_key=True)
# # 	title= db.Column(db.String(255))
# # 	content=db.Column(db.Text)
# # 	start_date=db.Column(db.DateTime)
# # 	end_date=db.Column(db.DateTime)
# # 	organizers=db.Column(db.String(255))
# # 	published_at=db.Column(db.DateTime)
# # 	price=db.Column(db.Integer)
# # 	photo=db.Column(db.String(255))
# # 	additional_info=db.Column(db.Text)
# # 	target_group=db.Column(db.String(255))
# # 	location=db.Column(db.Text)
# # 	district_id=db.Column(db.Integer, db.ForeignKey('raion.id'))
# # 	raion=db.relationship(Raion)
# # 	category=db.Column(db.String(255), db.ForeignKey('categorie.id'))
# # 	categorie=db.relationship(Categorie)
# # 	eventType=db.Column(db.String(255), db.ForeignKey('tipEveniment.id'))
# # 	tipEveniment=db.relationship(TipEveniment)
# # 	phone=db.Column(db.Integer)
# # 	email=bd.Column(db.String(255))


# # class Raion(db.Model):
# # 	id=db.Column(db.Integer, primary_key=True)
# # 	title=db.Column(db.String(255))

# # class Categorie(db.Model):
# # 	id=db.Column(db.Integer, primary_key=True)
# # 	title=db.Column(db.String(255))	

# # class TipEveniment(db.Model):
# # 	id=db.Column(db.Integer, primary_key=True)
# # 	title=db.Column(db.String(255))

# # class User(db.Model):
# # 	id=db.Column(db.Integer, primary_key=True)
# # 	name=db.Column(db.String(255))
# # 	password=dbColumn(db.Password)
# # 	email=db.Column(String(255))
# # 	type_id=db.Column(db.Integer, db.ForeignKey('user.id'))
# # 	user=db.relationship(User)

# # class User(db.Model):
# # 	id=db.Column(db.Integer, primary_key=True)
# # 	name=db.Column(db.Strind(255))
	
# class Event(db.Model):
# 	id = db.Column(db.Integer, primary_key = True)
# 	title = db.Column(db.String(255))
# 	content = db.Column(db.Text)
# 	start_date = db.Column(db.DateTime)
# 	end_date = db.Column(db.DateTime)
# 	organizer = db.Column(db.String(255))
# 	published_at = db.Column(db.DateTime, default=datetime.utcnow)
# 	price = db.Column(db.Integer)
# 	# photo = db.Column(db.String(255))
# 	additional_info = db.Column(db.Text)
# 	target_group = db.Column(db.Text)
# 	location = db.Column(db.Text)
# 	phone = db.Column(db.Integer)
# 	email = db.Column(db.String(50))
	
# 	category_id =  db.Column(db.Integer, db.ForeignKey('category.id') ) 
# 	category = db.relationship('Category', 
# 		backref = db.backref('posts', lazy = 'dynamic'))
	
# 	district_id = db.Column(db.Integer, db.ForeignKey('district.id') ) 
# 	district =  db.relationship('District', 
# 		backref = db.backref('posts', lazy = 'dynamic'))
	
# 	type_event_id = db.Column(db.Integer, db.ForeignKey('type.id') ) 
# 	type_event =  db.relationship('Type', 
# 		backref = db.backref('posts', lazy = 'dynamic'))

# 	# def __init__(title, content, start_date, end_date, organizer, published_at,
# 	# 	price, phone, additional_info, target_group, location, photo, email)


# class Category(db.Model):
# 	id = db.Column(db.Integer, primary_key = True)
# 	name = db.Column(db.String(255))
	
# class District(db.Model):
# 	id = db.Column(db.Integer, primary_key = True)
# 	name = db.Column(db.String(255))

# class Type(db.Model):
# 	id = db.Column(db.Integer, primary_key = True)
# 	name = db.Column(db.String(255))	

class EventImage(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	event_id = db.Column(db.Integer, db.ForeignKey('events.id') )
	event = db.relationship('Event', 
		backref = db.backref('images', lazy = 'dynamic'))
	image_link= db.Column(db.Text)

	def __str__(self):
		return 'event_id: {}, image_link: {}'.format(self.event_id, self.image_link)
