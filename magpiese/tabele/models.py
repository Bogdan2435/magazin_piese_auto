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
    loc_munca = models.ForeignKey(LocuriMunca, null=True, on_delete = models.PROTECT)

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


class Piesa_Model(models.Model):
    piesa = models.ForeignKey(Piese, on_delete = models.CASCADE)
    model = models.ForeignKey(Modele_Masini, on_delete = models.CASCADE)

    ORIGINALA = (
        ('originala', 'originala'),
        ('compatibila', 'compatibila'),
    )

    originala = models.CharField(
        max_length = 20,
        choices = ORIGINALA,
        default = 'originala',
        help_text = 'Alegeti daca piesa este originala sau nu.'
    )

    class Meta:
        verbose_name = 'Legatura Piesa - Model'
        verbose_name_plural = 'Legaturi Piesa - Model'


class Masini(models.Model):
    vin = models.CharField(max_length=17, primary_key=True)
    nr_inmatriculare = models.CharField(max_length=10)
    an_fabricatie = models.PositiveSmallIntegerField()
    kilometraj = models.CharField(max_length = 9, default='0')

    class Meta:
        verbose_name = 'Masina'
        verbose_name_plural = 'Masini'

    def __str__(self):
        return self.nr_inmatriculare


class Adrese(models.Model):
    tara = models.CharField(max_length=255)
    judet = models.CharField(max_length=255)
    localitate = models.CharField(max_length=255)
    strada = models.CharField(max_length=255)
    nr_strada = models.IntegerField(default ='0')
    nr_bloc = models.IntegerField(default ='0')
    scara = models.CharField(max_length=255, default =' ')
    etaj = models.IntegerField(default ='0')
    apartament = models.IntegerField(default ='0')

    class Meta:
        verbose_name = 'Adresa'
        verbose_name_plural = 'Adrese'

    def __str__(self):
        return 'strada %s din localitatea %s judetul %s' % (self.strada, self.localitate, self.judet)


class Comenzi(models.Model):
    data_comanda = models.DateField()
    masina_nr = models.ForeignKey(Masini, on_delete = models.PROTECT)
    client_nume = models.ForeignKey(Clienti, on_delete = models.PROTECT)
    angajat_nume = models.ForeignKey(Angajati, on_delete = models.PROTECT)

    TIP_LIVRARE = (
        ('ridicare personala', 'ridicare personala'),
        ('livrare', 'livrare'), 
    ) 

    mod_livrare = models.CharField(
        max_length = 20,
        choices = TIP_LIVRARE,
        default = 'livrare',
    )

    STATUS_COMANDA = (
        ('plasata', 'plasata'),
        ('pregatita pentru ridicare', 'pregatita pentru ridicare'),
        ('in curs de livrare', 'in curs de livrare'),
        ('ridicata', 'ridicata'),
        ('livrata', 'livrata')
    )

    status_comanda = models.CharField(
        max_length = 30,
        choices = STATUS_COMANDA,
        default = 'plasata',
    )

    class Meta:
        verbose_name = 'Comanda'
        verbose_name_plural = 'Comenzi'

    def __str__(self):
        return 'comanda din data %s cu id-ul %s' % (self.data_comanda, self.pk)


class ComandaPiesa(models.Model):
    comanda = models.ForeignKey(Comenzi, on_delete = models.CASCADE)
    piesa = models.ForeignKey(Piese, on_delete = models.CASCADE)
    nr_piese = models.IntegerField(default = '1')

    class Meta:
        verbose_name = 'Legatura Comanda - Piesa'
        verbose_name_plural = 'Legaturi Comenzi - Piese'


class Livrari(models.Model):
    awb = models.CharField(
        max_length = 20,
        primary_key = True,
    )
    angajat = models.ForeignKey(Angajati, on_delete = models.PROTECT)
    comanda = models.ForeignKey(Comenzi, on_delete = models.CASCADE)
    adresa = models.ForeignKey(Adrese, on_delete = models.PROTECT)

    STATUS_LIVRARE = (
        ('primita', 'primita'),
        ('in curs de livrare', 'in curs de livrare'),
        ('livrata', 'livrata'),
    )

    status_livrare = models.CharField(
        max_length = 30,
        choices = STATUS_LIVRARE,
        default = 'primita',
    )

    data_programata_livrare = models.DateField()

    class Meta:
        verbose_name = 'Livrare'
        verbose_name_plural = 'Livrari'


