from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, SubmitField, DateTimeField, FileField, IntegerField, PasswordField 
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from models import Category 
from models import District
from models import TypeEvent
from models import TargetGroup



class SignupForm(Form):
	nume = TextField('Nume')
	email = TextField('Email')
	type_id = QuerySelectField ('Alege tipul utilizatorului', query_factory=lambda: TypeEvent.query, get_label='name', allow_blank=True)
	parola = PasswordField('Parola')
	confirma_parola = PasswordField('Confirma Parola')
	submit = SubmitField('Sign Up')

class EventForm(Form):
	titlu = TextField('Titlul evenimentului')
	start_date = DateTimeField('Inceputul evenimentului')
	end_date = DateTimeField('Sfirsitul evenimentului')
	organizers = TextField('Organizatorii')
	published_at = DateTimeField('Publicat la...')
	price = IntegerField('Pretul evenimentului')
	photo = FileField('Poza evenimentului')	
	additional_info = TextField('Informatie aditionala')
	location = TextField('Locatia')
	phone = IntegerField('Numarul de telefon')
	district_id = QuerySelectField ('Alege unitatea administrativa', query_factory=lambda: District.query, get_label='name', allow_blank=True)
	category_id = QuerySelectField ('Alege categoria', query_factory=lambda: Category.query, get_label='name', allow_blank=True)
	type_event_id = QuerySelectField ('Alege tipul evenimentului', query_factory=lambda: TypeEvent.query, get_label='name', allow_blank=True)
	target_group_id = QuerySelectField ('Alege grupul tinta', query_factory=lambda: TargetGroup.query, get_label='name', allow_blank=True)
	submit = SubmitField('Submit')




	
		