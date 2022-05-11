from django.contrib import admin

from tabele.models import Adrese, Angajati, Clienti, LocuriMunca, Modele_Masini, Piesa_Model, Piese

class PiesaModelInline(admin.TabularInline):
    model = Piesa_Model
    extra = 1

class PieseAdmin(admin.ModelAdmin):
    inlines = (PiesaModelInline, )
    model = Piese

class ModeleMasiniAdmin(admin.ModelAdmin):
    inlines = (PiesaModelInline, )
    model = Modele_Masini

admin.site.register(LocuriMunca)
admin.site.register(Angajati)
admin.site.register(Adrese)
admin.site.register(Clienti)
admin.site.register(Modele_Masini, ModeleMasiniAdmin)
admin.site.register(Piese, PieseAdmin)
# admin.site.register(Piesa_Model)