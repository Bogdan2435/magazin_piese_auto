# from attr import field
from django import forms
from django.forms import ModelForm
from .models import *

class LocMuncaForm(forms.ModelForm):
    class Meta:
        model = LocuriMunca
        fields = "__all__"

class AngajatiForm(forms.ModelForm):
    class Meta:
        model = Angajati
        fields = "__all__"