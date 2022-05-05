from django.contrib import admin

from tabele.models import Adrese, Angajati, LocuriMunca

# Register your models here.

admin.site.register(LocuriMunca)
admin.site.register(Angajati)
admin.site.register(Adrese)