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
    data_angajare = forms.DateField(widget = forms.DateInput(attrs = {'class': 'form-control form-control-lg'}))
    data_nasterii = forms.DateField(widget = forms.DateInput(attrs = {'class': 'form-control form-control-lg'}))
    loc_munca = forms.ModelChoiceField(queryset = LocuriMunca.objects.all(), widget = forms.Select(attrs = {'class': 'form-control form-control-lg'}))

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

MOTORIZARI = (
        ('benzina', 'benzina'),
        ('diesel', 'diesel'),
        ('hybrid-benzina', 'hybrid-benzina'),
        ('hybrid-diesel', 'hybrid-diesel'),
        ('electric', 'electric'),
        ('hidrogen', 'hidrogen'),
    )

SISTEM_TRACTIUNE = (
    ('fata', 'fata'),
    ('spate', 'spate'),
    ('4x4', '4x4')
)

class ModeleForm(forms.ModelForm):
    marca = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control form-control-lg'}))
    model = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control form-control-lg'}))
    an_incepere_productie = forms.IntegerField(widget = forms.NumberInput(attrs = {'class': 'form-control form-control-lg'}))
    an_finalizare_productie = forms.IntegerField(widget = forms.NumberInput(attrs = {'class': 'form-control form-control-lg'}))
    motorizare_cc = forms.IntegerField(widget = forms.NumberInput(attrs = {'class': 'form-control form-control-lg'}))
    putere_cp = forms.IntegerField(widget = forms.NumberInput(attrs = {'class': 'form-control form-control-lg'}))
    combustibil = forms.ChoiceField(choices = MOTORIZARI, widget = forms.Select(attrs = {'class': 'form-control form-control-lg'})) 
    cod_motor = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control form-control-lg'})) 
    tip_tractiune = forms.ChoiceField(choices = SISTEM_TRACTIUNE,widget = forms.Select(attrs = {'class': 'form-control form-control-lg'})) 

    class Meta:
        model = Modele_Masini
        fields = "__all__"


class PieseForm(forms.ModelForm):
    denumire = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control form-control-lg'}))
    producator = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control form-control-lg'}))
    interval_recomandat_schimb = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control form-control-lg'}))
    pret_ron = forms.IntegerField(widget = forms.NumberInput(attrs = {'class': 'form-control form-control-lg'}))

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