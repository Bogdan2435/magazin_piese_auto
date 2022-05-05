from statistics import mode
from tabnanny import verbose
from django.db import models

# Create your models here.

class LocuriMunca(models.Model):
    denumire = models.CharField(max_length=255)
    salariu_min = models.IntegerField()
    salariu_max = models.IntegerField()

    class Meta:
        verbose_name = 'Loc munca'
        verbose_name_plural = 'Locuri munca'
        
    def __str__(self):
        return self.denumire

class Angajati(models.Model):
    nume_familie = models.CharField(max_length=255)
    prenume = models.CharField(max_length=255)
    salariu = models.IntegerField()
    email = models.CharField(max_length=255)
    data_angajare = models.DateField()
    data_nasterii = models.DateField()
    loc_munca = models.ForeignKey(LocuriMunca, on_delete = models.PROTECT)

    class Meta:
        verbose_name = 'Angajat'
        verbose_name_plural = 'Angajati'

    def __str__(self):
        return '%s %s' % (self.nume_familie, self.prenume)

class Adrese(models.Model):
    tara = models.CharField(max_length=255)
    judet = models.CharField(max_length=255)
    localitate = models.CharField(max_length=255)
    strada = models.CharField(max_length=255)
    nr_strada = models.IntegerField()
    nr_bloc = models.IntegerField()
    scara = models.CharField(max_length=255)
    etaj = models.IntegerField()
    apartament = models.IntegerField()

    class Meta:
        verbose_name = 'Adresa'
        verbose_name_plural = 'Adrese'

    def __str__(self):
        return 'strada %s din localitatea %s judetul %s' % (self.strada, self.localitate, self.judet)


