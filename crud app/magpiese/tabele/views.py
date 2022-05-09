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

