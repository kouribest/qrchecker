from django import forms
from django.db import models
from django.forms import ModelForm
from mali_project.models import formModel
from django_countries.widgets import CountrySelectWidget

class Formulaire(forms.ModelForm):
    class Meta:
        model = formModel
        field= '__all__'
      	exclude= []

