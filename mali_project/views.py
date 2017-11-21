from django.http import HttpResponse
from django.shortcuts import render_to_response, render, redirect
from datetime import datetime
from mali_project.forms import Formulaire
from mali_project.models import formModel
from django.http import JsonResponse
import re
import qrcode


def home(request):
	formulaire= Formulaire()
	return render(request, 'mali_project/index.html', {'form':formulaire})

def validate(request):
	#initialise a dict of all type field regex
	regex_dict={
		'date_regex': """(\d{2}[\/]){2}\d{4}""",
		'text_regex': '\w+',
	} 
	target = request.GET.get('trigger') #get input which triggered ajax event

	target_value= request.GET.get('value') #get the value 

	#the response to send after all process
	send_response={}
	message=''
	date_used= False

	if 'Date' in target: #if target is a date type
		p=re.compile(regex_dict['date_regex'])
		date_used= True #use date regex 
	else:
		p=re.compile(regex_dict['text_regex']) #otherwise it's a text type

	if p.match(target_value):
		send_response= {
			'is_ok': True,
			'message': 'Champs valide',
		}
	else:
		if date_used:
			message='le format de date soit etre Jour/Mois/Annee'
		else:
			message='Format de champ de invalide'
			send_response= {
				'is_ok': False,
				'message': message,
			}

	return JsonResponse(send_response)
# Method that generate the qrcode associated to id of each form 
def qrcodeGenese(request):
	
	data= request.GET.get('trigger')
	qr= qrcode.QRCode(
		version=2,
		error_correction= qrcode.constants.ERROR_CORRECT_H,
		box_size=30,
		border=4,
		)
	qr.add_data(data)
	qr.make(fit=True)
	img= qr.make_image()
	path='/Users/soumailakouriba/mali_project/mali_project/static/img/'+str(data)+'.jpeg'
	img.save(path)
	return JsonResponse({
		'path':path
		})

def addForm(request):
	#creating and processing the form
	form_process= Formulaire(request.POST or None)
	if form_process.is_valid():
		instance= form_process.save();
		instance.save()
		return HttpResponse('ok')
	else:
		return HttpResponse('non')

def scanView(request):
	return render(request, 'mali_project/scan.html')







	
	

	

