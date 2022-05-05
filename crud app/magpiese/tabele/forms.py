# from attr import field
from django import forms
from django.forms import ModelForm
from .models import *

class LocMuncaForm(forms.ModelForm):
    class Meta:
        model = LocuriMunca
        fields = "__all__"