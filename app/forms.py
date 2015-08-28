from flask.ext.wtf import Form 
from wtforms import TextField, IntegerField,\
	 PasswordField, SubmitField, DateTimeField, FileField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from models import Category
from models import District
from models import TypeEvent
from models import TargetGroup 
from models import Category


class  SignupForm(Form):
	nume = TextField('Nume')
	prenume = TextField('Prenume')
	organizatia = TextField('Organizatia')
	email = TextField ('Email')
	parola = PasswordField ('Parola')
	confirma_parola = PasswordField ('Confirma Parola')
	submit = SubmitField ('Sign Up') 

class  EventForm(Form):
	titlu = TextField('Titlu')
	content = TextField('Cotinut')
	start_date = DateTimeField('Data cind incepe evenimentul')
	end_date = DateTimeField('Cind se termina evenimentul')
	organizers = TextField('Organizat de ')
	published_at = DateTimeField('Publicat')
	price = IntegerField('Pret') 
	photo = TextField('Incarca o poza')
	additional_info = TextField('Informatii adaugatoare')
	location = TextField('Locatia')
	phone = IntegerField('Numar de Telefon')
	email = TextField('Email')
	category_id = QuerySelectField('category_list',query_factory=lambda: Category.query, get_label='name',allow_blank=True)
	district_id = QuerySelectField('Alege raionul',query_factory=lambda: District.query, get_label='name',allow_blank=True)
	type_event_id = QuerySelectField('Tipul evenimentului', query_factory=lambda: TypeEvent.query, get_label='name',allow_blank=True)
	target_group_id = QuerySelectField('Grupul Tinta', query_factory=lambda: TargetGroup.query, get_label='name',allow_blank=True)

class AddCategoryForm(Form):
	name = TextField('Adauga o categorie noua')
	submit = SubmitField ('Salveaza o  categorie noua') 
	photo = TextField('Adresa imaginii')
