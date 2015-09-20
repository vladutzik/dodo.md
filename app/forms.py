	# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, SubmitField, DateTimeField, FileField, IntegerField, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from models import Category 
from models import District
from models import TypeEvent
from models import TargetGroup, UserType


class SignupForm(Form):
	nume = TextField('Nume')
	email = TextField('Email')
	user_type_id = QuerySelectField ('Alege tipul utilizatorului', query_factory=lambda: UserType.query, get_label='name', allow_blank=True)
	parola = PasswordField('Parola')
	confirma_parola = PasswordField('Confirma Parola')
	submit = SubmitField('Sign Up')

class EventForm(Form):
	titlu = TextField('Titlul evenimentului')
	start_date = DateTimeField('Inceputul evenimentului')
	end_date = DateTimeField('Sfirsitul evenimentului')
	organizers = TextField('Organizatorii')
	# published_at = DateTimeField('Publicat la...')
	price = IntegerField('Pretul evenimentului')
	photo = TextField('Poza evenimentului')	
	content = TextAreaField('Descrierea evenmentului')
	additional_info = TextField('Informatie aditionala')
	location = TextField('Locatia')
	phone = IntegerField('Numarul de telefon')
	district_id = QuerySelectField ('Alege unitatea administrativa', query_factory=lambda: District.query, get_label='name', allow_blank=True)
	category_id = QuerySelectField ('Alege categoria', query_factory=lambda: Category.query, get_label='name', allow_blank=True)
	type_event_id = QuerySelectField ('Alege tipul evenimentului', query_factory=lambda: TypeEvent.query, get_label='name', allow_blank=True)
	target_group_id = QuerySelectField ('Alege grupul tinta', query_factory=lambda: TargetGroup.query, get_label='name', allow_blank=True)
	submit = SubmitField('Submit')


class AddCategoryForm(Form):
	name = TextField('Adauga o categorie noua')
	submit = SubmitField ('Salveaza o  categorie noua') 
	photo = TextField('Adresa imaginii')

class SigninForm(Form):
	nume = TextField("Nume")
	parola = PasswordField("Parola")
	user_type_id = QuerySelectField ('Alege tipul utilizatorului', query_factory=lambda: UserType.query, get_label='name', allow_blank=True)
	submit = SubmitField("Log in")

class AddImageToEvent(Form):
	title = TextField("Titlu:")
	image_link = TextField("Adauga link")
	submit = SubmitField("Ok")


class ContactUsForm(Form):
	name = TextField("Nume:")
	email = TextField("Email:")
	subject = TextField("Subiect:")
	message=TextField("Mesaj:")
	submit = SubmitField("Ok")	
