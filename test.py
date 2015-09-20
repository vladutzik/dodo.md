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
			result[key] = value.decode('utf-8')
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
	db.create_all()
	district_list = [{'name': 'Chişinău'},{'name': 'Bălţi'},{'name': 'Comrat'},{'name': 'Tiraspol'},{'name': 'Tighina (Bender)'},{'name': 'Anenii Noi'},{'name': 'Basarabeasca'},{'name': 'Briceni'},{'name': 'Cahul'},{'name': 'Călăraşi'},{'name': 'Cantemir'},{'name': 'Căuşeni'},{'name': 'Cimişlia'},{'name': 'Criuleni'},{'name': 'Donduşeni'},{'name': 'Drochia'},{'name': 'Dubăsari'},{'name': 'Edineţ'},{'name': 'Făleşti'},{'name': 'Floreşti'},{'name': 'Glodeni'},{'name': 'Hînceşti'},{'name': 'Ialoveni'},{'name': 'Leova'},{'name': 'Nisporeni'},{'name': 'Ocniţa'},{'name': 'Orhei'},{'name': 'Rezina'},{'name': 'Rîşcani'},{'name': 'Sîngerei'},{'name': 'Şoldăneşti'},{'name': 'Soroca'},{'name': 'Ştefan Vodă'},{'name': 'Străşeni'},{'name': 'Taraclia'},{'name': 'Teleneşti'},{'name': 'Ungheni'}]
	categorii_list = [{'name':'Robotică', 'icon':'pixeden pd-icon-robotics'}, {'name':'Fizică', 'icon':'pixeden pd-icon-science'},
					 {'name':'Astronomie', 'icon':'pixeden pd-icon-astronomy'}, {'name':'Informatică', 'icon':'pixeden pd-icon-IT'},
					 {'name':'Matematică', 'icon':'pixeden pd-icon-math'}, {'name':'Sănătate', 'icon':'pixeden pd-icon-health'},
					 {'name':'Ecologie', 'icon':'pixeden pd-icon-ecology'}, {'name':'Erudiție', 'icon':'pixeden pd-icon-knowledge'},
					 {'name':'Voluntariat', 'icon':'pixeden pd-icon-volunteer'}, {'name':'Limbi străine', 'icon':'pixeden pd-icon-language'},
					 {'name':'Literatură', 'icon':'pixeden pd-icon-literature'}, {'name':'Muzică', 'icon':'pixeden pd-icon-music'},
					 {'name':'Sport', 'icon':'pixeden pd-icon-sport'}, {'name':'Artă plastică', 'icon':'pixeden pd-icon-art'},
					 {'name':'Artă dramatică', 'icon':'pixeden pd-icon-drama'}]
	target_group_list = [{'name':'Elevi gimnaziu'}, {'name':'Elevi liceu'}, {'name':'Studenți'},{'name':'Voluntari'}]
	event_type_list = [{'name':'Eveniment'}, {'name':'Workshop'}, {'name':'Training'}, {'name':'Proiect'}, {'name':'Olimpiadă'}, {'name':'Club'}, {'name':'Curs'}, {'name':'Concurs'}, {'name':'Conferință'}, {'name':'Tabară de vară'}]
	user_type_list = [{'name':'ONG'}, {'name':'Persoană fizică'}, {'name':'Asociație obștească'}]

	insert_to_db(serialize_models(TargetGroup, target_group_list))
	insert_to_db(serialize_models(TypeEvent, event_type_list))
	insert_to_db(serialize_models(District, district_list))
	insert_to_db(serialize_models(Category, categorii_list))
	insert_to_db(serialize_models(UserType, user_type_list))

	#app.run(debug=True)