# Generated by Django 4.0.4 on 2022-05-10 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabele', '0006_clienti'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modele_Masini',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('an_incepere_productie', models.PositiveSmallIntegerField()),
                ('an_finalizare_productie', models.PositiveSmallIntegerField()),
                ('motorizare_cc', models.IntegerField(null=True)),
                ('putere_cp', models.IntegerField()),
                ('combustibil', models.CharField(choices=[('benzina', 'benzina'), ('diesel', 'diesel'), ('hybrid-benzina', 'hybrid-benzina'), ('hybrid-diesel', 'hybrid-diesel'), ('electric', 'electric'), ('hidrogen', 'hidrogen')], default='benzina', help_text='Alegeti combustibilul masinii', max_length=20)),
                ('cod_motor', models.CharField(max_length=255)),
                ('tip_tractiune', models.CharField(choices=[('fata', 'fata'), ('spate', 'spate'), ('4x4', '4x4')], default='fata', help_text='Alegeti tipul de tractiune al masinii', max_length=20)),
            ],
        ),
    ]
