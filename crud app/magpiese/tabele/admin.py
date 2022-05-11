from django.contrib import admin

from tabele.models import Adrese, Angajati, Clienti, LocuriMunca, Modele_Masini, Piese

# Register your models here.

admin.site.register(LocuriMunca)
admin.site.register(Angajati)
admin.site.register(Adrese)
admin.site.register(Clienti)
admin.site.register(Modele_Masini)
admin.site.register(Piese)