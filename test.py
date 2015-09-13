 # -*- coding: utf-8 -*-
from app.models import *
from app import db

def insert_to_db(models_list):
	for item in models_list:
		db.session.add(item)
	db.session.commit()

def sanitize(item):
	result = {}
	for key, value in item.iteritems():
		try: 
			result[key] = value.decode('latin-1')
		except AttributeError:
			pass
	return result

def serialize_models(model, data):
	model_list = []
	for item in data:
		model_item = model(**sanitize(item))
		model_list.append(model_item)
	return model_list


if __name__ == '__main__':
	district_list = [{'name': 'Chişinău'},{'name': 'Bălţi'},{'name': 'Comrat'},{'name': 'Tiraspol'},{'name': 'Tighina (Bender)'},{'name': 'Anenii Noi'},{'name': 'Basarabeasca'},{'name': 'Briceni'},{'name': 'Cahul'},{'name': 'Călăraşi'},{'name': 'Cantemir'},{'name': 'Căuşeni'},{'name': 'Cimişlia'},{'name': 'Criuleni'},{'name': 'Donduşeni'},{'name': 'Drochia'},{'name': 'Dubasari'},{'name': 'Edineţ'},{'name': 'Făleşti'},{'name': 'Floreşti'},{'name': 'Glodeni'},{'name': 'Hînceşti'},{'name': 'Ialoveni'},{'name': 'Leova'},{'name': 'Nisporeni'},{'name': 'Ocniţa'},{'name': 'Orhei'},{'name': 'Rezina'},{'name': 'Rîşcani'},{'name': 'Sîngerei'},{'name': 'Şoldăneşti'},{'name': 'Soroca'},{'name': 'Ştefan Vodă'},{'name': 'Străşeni'},{'name': 'Taraclia'},{'name': 'Teleneşti'},{'name': 'Ungheni'}]
	categorii_list = [{'name':'Robotică'}, {'name':'Fizică'}, {'name':'Astronomie'}, {'name':'Informatică'}, {'name':'Matematică'}, {'name':'Sănătate'}, {'name':'Ecologie'}, {'name':'Erudiție'}, {'name':'Voluntariat'}, {'name':'Limbi străine'}, {'name':'Literatură'}, {'name':'Muzică'}, {'name':'SPort'}, {'name':'Artă plastică'}, {'name':'Artă dramatică'}]
	target_group_list = [{'name':'Elevi gimnaziu'}, {'name':'Elevi liceu'}, {'name':'Studenti'},{'name':'Voluntari'}]
	event_type_list = [{'name':'Workshop'}, {'name':'Training'}, {'name':'Proiect'}, {'name':'Olimpiada'}, {'name':'Club'}, {'name':'Curs'}, {'name':'Concurs'}, {'name':'Conferinta'}, {'name':'Tabara de vara'}]

	user_type_list = [{'name':'ONG'}, {'name':'Persoana fizica'}, {'name':'Asociatie obsteasca'}]
	insert_to_db(serialize_models(TargetGroup, target_group_list))
	insert_to_db(serialize_models(TypeEvent, event_type_list))
	insert_to_db(serialize_models(District, district_list))
	insert_to_db(serialize_models(Category, categorii_list))
	insert_to_db(serialize_models(UserType, user_type_list))
