from app import db

# class Eveniment(db.Model):
# 	id=db.Column(db.Integer, primary_key=True)
# 	title= db.Column(db.String(255))
# 	content=db.Column(db.Text)
# 	start_date=db.Column(db.DateTime)
# 	end_date=db.Column(db.DateTime)
# 	organizers=db.Column(db.String(255))
# 	published_at=db.Column(db.DateTime)
# 	price=db.Column(db.Integer)
# 	photo=db.Column(db.String(255))
# 	additional_info=db.Column(db.Text)
# 	target_group=db.Column(db.String(255))
# 	location=db.Column(db.Text)
# 	district_id=db.Column(db.Integer, db.ForeignKey('raion.id'))
# 	raion=db.relationship(Raion)
# 	category=db.Column(db.String(255), db.ForeignKey('categorie.id'))
# 	categorie=db.relationship(Categorie)
# 	eventType=db.Column(db.String(255), db.ForeignKey('tipEveniment.id'))
# 	tipEveniment=db.relationship(TipEveniment)
# 	phone=db.Column(db.Integer)
# 	email=bd.Column(db.String(255))


# class Raion(db.Model):
# 	id=db.Column(db.Integer, primary_key=True)
# 	title=db.Column(db.String(255))

# class Categorie(db.Model):
# 	id=db.Column(db.Integer, primary_key=True)
# 	title=db.Column(db.String(255))	

# class TipEveniment(db.Model):
# 	id=db.Column(db.Integer, primary_key=True)
# 	title=db.Column(db.String(255))

# class User(db.Model):
# 	id=db.Column(db.Integer, primary_key=True)
# 	name=db.Column(db.String(255))
# 	password=dbColumn(db.Password)
# 	email=db.Column(String(255))
# 	type_id=db.Column(db.Integer, db.ForeignKey('user.id'))
# 	user=db.relationship(User)

# class User(db.Model):
# 	id=db.Column(db.Integer, primary_key=True)
# 	name=db.Column(db.Strind(255))
	