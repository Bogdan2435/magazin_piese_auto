from email.policy import default
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


ORIGINALA = (
        ('originala', 'originala'),
        ('compatibila', 'compatibila'),
    )


class PiesaModelForm(forms.ModelForm):
    piesa = forms.ModelChoiceField(queryset = Piese.objects.all(), widget = forms.Select(attrs = {'class': 'form-control form-control-lg'}))
    model = forms.ModelChoiceField(queryset = Modele_Masini.objects.all(), widget = forms.Select(attrs = {'class': 'form-control form-control-lg'}))
    originala = forms.ChoiceField(choices = ORIGINALA, widget = forms.Select(attrs = {'class': 'form-control form-control-lg'}))

    class Meta:
        model = Piesa_Model
        fields = "__all__"


class MasiniForm(forms.ModelForm):
    vin = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control form-control-lg'}))
    nr_inmatriculare = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control form-control-lg'}))
    an_fabricatie = forms.IntegerField(widget = forms.NumberInput(attrs = {'class': 'form-control form-control-lg'}))
    kilometraj = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control form-control-lg'}))

    class Meta:
        model = Masini
        fields = "__all__"


class ComenziForm(forms.ModelForm):
    data_comanda = forms.DateField(widget = forms.DateInput(attrs = {'class': 'form-control form-control-lg'}))
    masina_nr = forms.ModelChoiceField(queryset = Masini.objects.all(), widget = forms.Select(attrs = {'class': 'form-control form-control-lg'}))
    client_nume = forms.ModelChoiceField(queryset = Clienti.objects.all(), widget = forms.Select(attrs = {'class': 'form-control form-control-lg'}))
    angajat_nume = forms.ModelChoiceField(queryset = Angajati.objects.all(), widget = forms.Select(attrs = {'class': 'form-control form-control-lg'}))


    class Meta:
        model = Comenzi
        fields = "__all__"


class ComandaPiesaForm(forms.ModelForm):
    piesa = forms.ModelChoiceField(queryset = Piese.objects.all(), widget = forms.Select(attrs = {'class': 'form-control form-control-lg'}))
    comanda = forms.ModelChoiceField(queryset = Comenzi.objects.all(), widget = forms.Select(attrs = {'class': 'form-control form-control-lg'}))
    nr_piese = forms.IntegerField(widget = forms.NumberInput(attrs = {'class': 'form-control form-control-lg'}))

    class Meta:
        model = ComandaPiesa
        fields = "__all__"


class AdreseForm(forms.ModelForm):
    tara = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control form-control-lg'}))
    judet = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control form-control-lg'}))
    localitate = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control form-control-lg'}))
    strada = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control form-control-lg'}))
    nr_strada = forms.IntegerField(widget = forms.NumberInput(attrs = {'class': 'form-control form-control-lg'}))
    nr_bloc = forms.IntegerField(widget = forms.NumberInput(attrs = {'class': 'form-control form-control-lg'}))
    scara = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control form-control-lg'}))
    etaj = forms.IntegerField(widget = forms.NumberInput(attrs = {'class': 'form-control form-control-lg'}))
    apartament = forms.IntegerField(widget = forms.NumberInput(attrs = {'class': 'form-control form-control-lg'}))

    class Meta:
        model = Adrese
        fields = "__all__"


STATUS_LIVRARE = (
        ('primita', 'primita'),
        ('in curs de livrare', 'in curs de livrare'),
        ('livrata', 'livrata'),
    )


class LivrariForm(forms.ModelForm):
    awb = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control form-control-lg'}))
    angajat = forms.ModelChoiceField(queryset = Angajati.objects.all(), widget = forms.Select(attrs = {'class': 'form-control form-control-lg'}))
    comanda = forms.ModelChoiceField(queryset = Comenzi.objects.all(), widget = forms.Select(attrs = {'class': 'form-control form-control-lg'}))
    adresa = forms.ModelChoiceField(queryset = Adrese.objects.all(), widget = forms.Select(attrs = {'class': 'form-control form-control-lg'}))
    status_livrare = forms.ChoiceField(choices = STATUS_LIVRARE, widget = forms.Select(attrs = {'class': 'form-control form-control-lg'}))
    data_programata_livrare = forms.DateField(widget = forms.DateInput(attrs = {'class': 'form-control form-control-lg'}))

    class Meta:
        model = Livrari
        fields = "__all__"