from django import forms
from .models import *


class LocMuncaForm(forms.ModelForm):

    denumire = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control form-control-lg'}))
    salariu_min = forms.IntegerField(widget = forms.NumberInput(attrs = {'class': 'form-control form-control-lg'}))
    salariu_max = forms.IntegerField(widget = forms.NumberInput(attrs = {'class': 'form-control form-control-lg'}))
    
    class Meta:
        model = LocuriMunca
        fields = "__all__"
    


class AngajatiForm(forms.ModelForm):

    nume_familie = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control form-control-lg'}))
    prenume = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control form-control-lg'}))
    salariu = forms.IntegerField(widget = forms.NumberInput(attrs = {'class': 'form-control form-control-lg'}))
    email = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control form-control-lg'}))
    data_angajare = forms.DateField(widget = forms.DateInput(attrs = {'class': 'form-control form-control-lg', 'data-toggle': 'datepicker-icon'}))
    data_nasterii = forms.DateField(widget = forms.DateInput(attrs = {'class': 'form-control form-control-lg', 'data-toggle': 'datepicker-icon'}))
    # loc_munca = forms.ChoiceField(queryset=LocuriMunca.objects.all(), widget = forms.Select(attrs = {'class': 'form-control form-control-lg'}))

    class Meta:
        model = Angajati
        fields = "__all__"

    widget = {
        'loc_munca': forms.Select(attrs = {'class': 'form-control form-control-lg'})
    }



class ClientiForm(forms.ModelForm):

    cnp = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control form-control-lg'}))
    nume_familie = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control form-control-lg'}))
    prenume = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control form-control-lg'}))
    nr_telefon = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control form-control-lg'}))
    email = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control form-control-lg'}))

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