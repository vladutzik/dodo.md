from flask.ext.wtf import Form
from wtforms.fields import TextField, IntegerField,PasswordField, SubmitField, DateTimeField, StringField

# class EventForm(Form):
# 	title=TextField('Titlu')
# 	content=TextField('Descriere')
# 	start_date=DateTimeField('&#206nceputul evenimentului')
# 	end_date=DateTimeField('Sf&#226r&#351itul evenimentului')
# 	organizers=TextField('Organizatori')	
# 	published_at=DateTimeField('Data public&#259rii')
# 	price=IntegerField('Pre 	&#355')
# 	photo=StringField('Poz&#259')
# 	additional_info=TextField("Informa 	&#355ie ad&#259ug&#259toare")
# 	target_group=TextField('Grup- 	&#355int&#259')
# 	location=TextField('Loc')
# 	district_id=IntegerField('Localitate')
# 	category=IntegerField('Categorie')
# 	eventType=IntegerField('Tipul evenimentului')
# 	phone=IntegerField('Num&#259rul de telefon')
# 	email=StringField('Email')

# class UserForm(Form):
# 	name=StringField('Nume complet:')
# 	password=PasswordField('Parolă:')
# 	email=StringField("Email:")
# 	type_id=IntegerField('Tip utilizator:')