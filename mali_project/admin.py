from mali_project.models import formModel
from django.contrib import admin
from mali_project.forms import Formulaire

class entryForm(admin.ModelAdmin):
	list_display= ['identifiant', 'Nom_famille', 'Prenom', 'Venant_de', 'Allant_a']

admin.site.register(formModel, entryForm)
