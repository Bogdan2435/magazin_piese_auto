from statistics import mode
from tabnanny import verbose
from django.db import models

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
    loc_munca = models.ForeignKey(LocuriMunca, null=True, on_delete = models.RESTRICT)

    class Meta:
        verbose_name = 'Angajat'
        verbose_name_plural = 'Angajati'

    def __str__(self):
        return '%s %s' % (self.nume_familie, self.prenume)

class Clienti(models.Model):
    cnp = models.CharField(max_length=13, primary_key=True)
    nume_familie = models.CharField(max_length=255)
    prenume = models.CharField(max_length=255)
    nr_telefon = models.CharField(max_length=12)
    email = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clienti'

    def __str__(self):
        return '%s %s' % (self.nume_familie, self.prenume)

class Modele_Masini(models.Model):
    marca = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    an_incepere_productie = models.PositiveSmallIntegerField()
    an_finalizare_productie = models.PositiveSmallIntegerField()
    motorizare_cc = models.IntegerField(
        default='0'
    )
    putere_cp = models.IntegerField()

    MOTORIZARI = (
        ('benzina', 'benzina'),
        ('diesel', 'diesel'),
        ('hybrid-benzina', 'hybrid-benzina'),
        ('hybrid-diesel', 'hybrid-diesel'),
        ('electric', 'electric'),
        ('hidrogen', 'hidrogen'),
    )

    combustibil = models.CharField(
        max_length = 20,
        choices = MOTORIZARI,
        default = 'benzina',
        help_text = 'Alegeti combustibilul masinii',
    )

    cod_motor = models.CharField(
        max_length=255,
        default='Nu exista'
)

    SISTEM_TRACTIUNE = (
        ('fata', 'fata'),
        ('spate', 'spate'),
        ('4x4', '4x4')
    )

    tip_tractiune = models.CharField(
        max_length = 20,
        choices = SISTEM_TRACTIUNE,
        default = 'fata',
        help_text = 'Alegeti tipul de tractiune al masinii',
    )

    class Meta:
        verbose_name = 'Model Masina'
        verbose_name_plural = 'Modele Masini'

    def __str__(self):
        return '%s %s an %s' % (self.marca, self.model, self.an_incepere_productie)

class Piese(models.Model):
    denumire = models.CharField(max_length=255)
    producator = models.CharField(max_length=255)
    interval_recomandat_schimb = models.CharField(max_length=255, default = "nu exista")
    pret_ron = models.IntegerField()

    class Meta:
        verbose_name = 'Piesa'
        verbose_name_plural = 'Piese'

    def __str__(self):
        return '%s produs de %s' % (self.denumire, self.producator)

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


