from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.

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
        'locMunca':locMunca,
        'form':form,
    }
    return render(request, 'update_locurimunca.html', context)

