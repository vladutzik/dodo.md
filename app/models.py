from app import db

class Category(db.Model):
	__tablename__ = 'categories'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))
	photo = db.Column(db.Text)

	def __init__(self, new_name):
		self.name = new_name

class District(db.Model):
	__tablename__ = 'districts'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))

class TypeEvent(db.Model):
	__tablename__ = 'typeevent'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))

class TargetGroup(db.Model):
	__tablename__ ='targetgroup'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))

class Eveniment(db.Model):
	__tablename__ = 'evenimente'
	id = db.Column(db.Integer, primary_key=True)
	titlu = db.Column(db.String(255))
	content = db.Column(db.Text)
	start_date = db.Column(db.DateTime)
	end_date = db.Column(db.DateTime)
	organizers = db.Column(db.String(255))
	published_at = db.Column(db.DateTime)
	price = db.Column(db.Integer)
	photo = db.Column(db.String(255))
	additional_info = db.Column(db.Text)
	target_group = db.Column(db.String(255))
	location = db.Column(db.Text)
	phone = db.Column(db.Integer)
	email = db.Column(db.String(50))
	category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
	category = db.relationship('Category', backref=db.backref('evenimente', order_by = id))
	district_id = db.Column(db.String(20), db.ForeignKey('districts.id'))
	district = db.relationship('District', backref=db.backref('evenimente', lazy='dynamic', order_by = id))
	type_event_id = db.Column(db.String(20), db.ForeignKey('typeevent.id'))
	type_event = db.relationship('TypeEvent', backref=db.backref('evenimente', lazy='dynamic', order_by = id))
	target_group_id = db.Column(db.String(20), db.ForeignKey('targetgroup.id'))