import os
from django.db import models
from django.contrib import admin
from datetime import datetime
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

genre=(
		('Homme','Homme'),
		('Femme','Femme'),
	)

class formModel(models.Model):
	identifiant= models.CharField(max_length=6, primary_key=True)
	Date_vol= models.DateField()
	Numero_vol= models.CharField(max_length=7)
	Numero_siege= models.CharField(max_length=50)
	Venant_de= models.CharField(max_length=50)
	Allant_a= models.CharField(max_length=50)

	Numero_passport= models.CharField(max_length=50)
	Date_delivrance_passport= models.DateField()
	Passport_emis_par= models.CharField(max_length=50)
	Date_expiration=models.CharField(max_length=50)
	Num_visa=models.CharField(max_length=50, default='N/C')
	Visa_delivre_par= models.CharField(max_length=20, default='N/C')
	Duree_validite=models.CharField(max_length=20, default='N/C')

	Nom_famille=models.CharField(max_length=50)
	Prenom=models.CharField(max_length=50)
	Date_naissance=models.DateField()
	Lieu_naissance= models.CharField(max_length=50)
	Genre= models.CharField(max_length=50, choices=genre)
	Nationalite= models.CharField(max_length=50)
	Profession= models.CharField(max_length=50)
	Telephone= models.CharField(max_length=13)
	Email= models.CharField(max_length=50)
	Adresse_locale= models.CharField(max_length=50)
	Adresse_Etranger= models.CharField(max_length=50)
	


		