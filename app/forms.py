 # -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import TextField, IntegerField, PasswordField, SubmitField, DateTimeField, FileField, FileField, FieldList,StringField
from app.widgets import DateTimePickerWidget
from wtforms.fields.html5 import DateTimeField

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


class RegisterForm(Form):
	nume = TextField("Nume")
	specie = TextField("Specie")
	virsta = IntegerField("Virsta")
	parola = PasswordField("Parola")
	confirma_parola = PasswordField("Confirma parola")
	submit = SubmitField("Sign up")

class SigninForm(Form):
	nume = TextField("Nume")
	parola = PasswordField("Parola")
	confirma_parola = PasswordField("Confirma parola")
	submit = SubmitField("Log in")

class SelectPhotoForm(Form):
	photo_link = TextField("Link fotografie")

class EventForm(Form):
	title = TextField("Titlu")
	content = TextField("Continut")
	start_date = DateTimeField("Data inceperii")
	end_date = DateTimeField("Data sfirsitului")
	organizer = TextField("Organizator")
	published_at = DateTimeField("Data publicarii")
	price = IntegerField("Pret")
	photo = TextField("Foto")
	# photo = FieldList(FormField(GuestForm))

	additional_info = TextField("Informatie aditionala")
	target_group = TextField("Grup tinta")
	location = TextField("Locul desfasurarii")
	phone = IntegerField("Grup tinta")
	email = TextField("Email")
	submit = SubmitField("Submit")

class AddImageToEvent(Form):
	title = TextField("Titlu:")
	image_link = TextField("Add image link:")
	submit = SubmitField("Ok")	