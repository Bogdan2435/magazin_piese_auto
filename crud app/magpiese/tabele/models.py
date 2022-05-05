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
        return self.name