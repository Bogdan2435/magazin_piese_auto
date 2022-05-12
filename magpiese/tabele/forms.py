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


class ClientiForm(forms.ModelForm):
    class Meta:
        model = Clienti
        fields = "__all__"


class ModeleForm(forms.ModelForm):
    class Meta:
        model = Modele_Masini
        fields = "__all__"


class PieseForm(forms.ModelForm):
    class Meta:
        model = Piese
        fields = "__all__"


class PiesaModelForm(forms.ModelForm):
    class Meta:
        model = Piesa_Model
        fields = "__all__"


class MasiniForm(forms.ModelForm):
    class Meta:
        model = Masini
        fields = "__all__"


class ComenziForm(forms.ModelForm):
    class Meta:
        model = Comenzi
        fields = "__all__"


class ComandaPiesaForm(forms.ModelForm):
    class Meta:
        model = ComandaPiesa
        fields = "__all__"


class AdreseForm(forms.ModelForm):
    class Meta:
        model = Adrese
        fields = "__all__"

class LivrariForm(forms.ModelForm):
    class Meta:
        model = Livrari
        fields = "__all__"