from django.shortcuts import render, redirect
from .forms import *
from .models import *


################### HOME #####################
def home(request):
    context = {}
    return render(request, 'home.html', context)


################### CREATE #####################
def create(request):
    context = {}
    return render(request, 'create.html', context)

def create_LocMunca(request):
    if request.method == "POST":
        form = LocMuncaForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('../create/')
            except:
                pass
    else:
        form = LocMuncaForm()
    return render(request, 'create_locurimunca.html', {'form':form}) 

def create_Angajat(request):
    if request.method == "POST":
        form = AngajatiForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('../create/')
            except:
                pass
    else:
        form = AngajatiForm()
    return render(request, 'create_angajati.html', {'form':form}) 

def create_Client(request):
    if request.method == "POST":
        form = ClientiForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('../create/')
            except:
                pass
    else:
        form = ClientiForm()
    return render(request, 'create_clienti.html', {'form':form})

def create_Model(request):
    if request.method == "POST":
        form = ModeleForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('../create/')
            except:
                pass
    else:
        form = ModeleForm()
    return render(request, 'create_modele.html', {'form':form})

def create_Piesa(request):
    if request.method == "POST":
        form = PieseForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('../create/')
            except:
                pass
    else:
        form = PieseForm()
    return render(request, 'create_piese.html', {'form':form})

def create_PiesaModel(request):
    if request.method == "POST":
        form = PiesaModelForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('../create/')
            except:
                pass
    else:
        form = PiesaModelForm()
    return render(request, 'create_piesamodel.html', {'form':form}) 


################### SEARCH #####################
def search(request):
    context = {}
    return render(request, 'search.html', context)

def read_Angajati(request):
    angajati = Angajati.objects.all()
    locuriMunca = LocuriMunca.objects.all()
    context = {
        'angajati': angajati,
        'locuriMunca': locuriMunca,
    }
    return render(request, 'search_angajati.html', context)

def read_LocuriMunca(request):
    locuriMunca = LocuriMunca.objects.all()
    context = {
        'locuriMunca':locuriMunca,
    }
    return render(request, 'search_locurimunca.html', context)

def read_Clienti(request):
    clienti = Clienti.objects.all()
    context = {
        'clienti': clienti,
    }
    return render(request, 'search_clienti.html', context)

def read_Modele(request):
    modele = Modele_Masini.objects.all()
    context = {
        'modele': modele,
    }
    return render(request, 'search_modele.html', context)

def read_Piese(request):
    piese = Piese.objects.all()
    context = {
        'piese': piese,
    }
    return render(request, 'search_piese.html', context)

def read_PiesaModel(request):
    piesaModel = Piesa_Model.objects.all()
    piese = Piese.objects.all()
    modele = Modele_Masini.objects.all()
    context = {
        'piesaModel': piesaModel,
        'piese': piese,
        'modele': modele,

    }
    return render(request, 'search_piesaModel.html', context)

################### UPDATE #####################
def update_LocuriMunca(request, pk):
    locMunca = LocuriMunca.objects.get(id=pk)
    form = LocMuncaForm(instance=locMunca)

    if request.method == 'POST':
        form = LocMuncaForm(request.POST, instance=locMunca)
        if form.is_valid():
            form.save()
            return redirect('/search/locurimunca')

    context = {
        'locMunca': locMunca,
        'form': form,
    }
    return render(request, 'update_locurimunca.html', context)

def update_Angajati(request, pk):
    angajat = Angajati.objects.get(id=pk)
    form = AngajatiForm(instance=angajat)

    if request.method == 'POST':
        form = AngajatiForm(request.POST, instance=angajat)
        if form.is_valid():
            form.save()
            return redirect('/search/angajati')

    context = {
        'angajat': angajat,
        'form': form,
    }
    return render(request, 'update_angajati.html', context)

def update_Clienti(request, pk):
    client = Clienti.objects.get(cnp=pk)
    form = ClientiForm(instance=client)

    if request.method == 'POST':
        form = ClientiForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('/search/clienti')

    context = {
        'client': client,
        'form': form,
    }
    return render(request, 'update_clienti.html', context)

def update_Modele(request, pk):
    modelMasina = Modele_Masini.objects.get(id=pk)
    form = ModeleForm(instance=modelMasina)

    if request.method == 'POST':
        form = ModeleForm(request.POST, instance=modelMasina)
        if form.is_valid():
            form.save()
            return redirect('/search/modele')

    context = {
        'modelMasina': modelMasina,
        'form': form,
    }
    return render(request, 'update_modele.html', context)

def update_Piese(request, pk):
    piesa = Piese.objects.get(id=pk)
    form = PieseForm(instance=piesa)

    if request.method == 'POST':
        form = PieseForm(request.POST, instance=piesa)
        if form.is_valid():
            form.save()
            return redirect('/search/piese')

    context = {
        'piesa': piesa,
        'form': form,
    }
    return render(request, 'update_piese.html', context)

def update_PiesaModel(request, pk):
    piesamodel = Piesa_Model.objects.get(id=pk)
    form = PiesaModelForm(instance=piesamodel)

    if request.method == 'POST':
        form = PiesaModelForm(request.POST, instance=piesamodel)
        if form.is_valid():
            form.save()
            return redirect('/search/piesamodel')

    context = {
        'piesamodel': piesamodel,
        'form': form,
    }
    return render(request, 'update_piesamodel.html', context)

################### DELETE #####################
def delete_LocuriMunca(request, pk):
    locMunca = LocuriMunca.objects.get(id=pk)

    if request.method == 'POST':
        locMunca.delete()
        return redirect('/search/locurimunca')

    context = {
        'locMunca': locMunca,
    }
    return render(request, 'delete_locurimunca.html', context)

def delete_Angajati(request, pk):
    angajat = Angajati.objects.get(id=pk)

    if request.method == 'POST':
        angajat.delete()
        return redirect('/search/angajati')

    context = {
        'angajat': angajat,
    }
    return render(request, 'delete_angajati.html', context)

def delete_Clienti(request, pk):
    client = Clienti.objects.get(cnp=pk)

    if request.method == 'POST':
        client.delete()
        return redirect('/search/clienti')

    context = {
        'client': client,
    }
    return render(request, 'delete_clienti.html', context)

def delete_Modele(request, pk):
    modelMasina = Modele_Masini.objects.get(id=pk)

    if request.method == 'POST':
        modelMasina.delete()
        return redirect('/search/modele')

    context = {
        'modelMasina': modelMasina,
    }
    return render(request, 'delete_modele.html', context)

def delete_Piese(request, pk):
    piesa = Piese.objects.get(id=pk)

    if request.method == 'POST':
        piesa.delete()
        return redirect('/search/piese')

    context = {
        'piesa': piesa,
    }
    return render(request, 'delete_piese.html', context)

def delete_PiesaModel(request, pk):
    piesamodel = Piesa_Model.objects.get(id=pk)
    piese = Piese.objects.all()
    modele = Modele_Masini.objects.all()

    if request.method == 'POST':
        piesamodel.delete()
        return redirect('/search/piesamodel')

    context = {
        'piesamodel': piesamodel,
        'piese': piese,
        'modele': modele,
    }
    return render(request, 'delete_piesamodel.html', context)

