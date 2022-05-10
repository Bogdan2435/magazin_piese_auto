from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.

def home(request):
    context = {}
    return render(request, 'home.html', context)

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
    return render(request, 'search_locurimunca.html', {'locuriMunca':locuriMunca})

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


