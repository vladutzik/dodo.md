 # -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import TextField, IntegerField, PasswordField, SubmitField, DateTimeField, FileField, FileField, FieldList,StringField
from app.widgets import DateTimePickerWidget
from wtforms.fields.html5 import DateTimeField


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

# class ContactUsForm(Form):
# 	name = TextField("Nume:")
# 	email = TextField("Email:")
# 	subject = TextField("Subiect:")
# 	message=TextField("Mesaj:")
# 	submit = SubmitField("Ok")	