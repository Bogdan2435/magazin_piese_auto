from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.

def create_LocMunca(request):
    if request.method == "POST":
        form = LocMuncaForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                # return redirect('search/')
            except:
                pass
    else:
        form = LocMuncaForm()
    return render(request, 'create.html', {'form':form}) 