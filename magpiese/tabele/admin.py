from django.contrib import admin

from tabele.models import Adrese, Angajati, Clienti, ComandaPiesa, Comenzi, LocuriMunca, Masini, Modele_Masini, Piesa_Model, Piese

class PiesaModelInline(admin.TabularInline):
    model = Piesa_Model
    extra = 1


class ModeleMasiniAdmin(admin.ModelAdmin):
    inlines = (PiesaModelInline, )
    model = Modele_Masini


class ComandaPiesaInline(admin.TabularInline):
    model = ComandaPiesa
    extra = 1

class PieseAdmin(admin.ModelAdmin):
    inlines = (PiesaModelInline, ComandaPiesaInline, )
    model = Piese

class ComenziAdmin(admin.ModelAdmin):
    inlines = (ComandaPiesaInline, )
    model = Comenzi

admin.site.register(LocuriMunca)
admin.site.register(Angajati)
admin.site.register(Adrese)
admin.site.register(Clienti)
admin.site.register(Modele_Masini, ModeleMasiniAdmin)
admin.site.register(Piese, PieseAdmin)
admin.site.register(Masini)
admin.site.register(Comenzi, ComenziAdmin)
# admin.site.register(Piesa_Model)